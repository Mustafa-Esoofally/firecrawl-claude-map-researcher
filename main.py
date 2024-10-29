import streamlit as st
import anthropic
from firecrawl import FirecrawlApp
import json
import re
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="Website Information Extractor",
    page_icon="🔍",
    layout="wide"
)

# Initialize session state for API keys
if 'api_keys_set' not in st.session_state:
    st.session_state.firecrawl_key = os.getenv('FIRECRAWL_API_KEY')
    st.session_state.anthropic_key = os.getenv('ANTHROPIC_API_KEY')
    st.session_state.api_keys_set = False

def initialize_clients():
    try:
        app = FirecrawlApp(api_key=st.session_state.firecrawl_key)
        client = anthropic.Anthropic(api_key=st.session_state.anthropic_key)
        st.session_state.api_keys_set = True
        return app, client
    except Exception as e:
        st.error(f"Error initializing clients: {str(e)}")
        return None, None

# Initialize clients on startup
if not st.session_state.api_keys_set:
    app, client = initialize_clients()

# Main content
st.title("Website Information Extractor 🔍")
st.markdown("Enter a website URL and your question to extract relevant information.")

# Input fields
url = st.text_input("Website URL", placeholder="https://example.com")
objective = st.text_input("What would you like to know?", placeholder="Find pricing plans")

def find_relevant_page_via_map(objective, url, app, client):
    try:
        with st.status("Searching website...") as status:
            status.write("Initiating search...")
            
            map_prompt = f"""
            The map function generates a list of URLs from a website and accepts a search parameter.
            Based on the objective of: {objective}, suggest a 1-2 word search parameter.
            """

            completion = client.messages.create(
                model='claude-3-5-sonnet-20241022',
                max_tokens=1000,
                temperature=0,
                system="Expert web crawler",
                messages=[{'role': 'user', 'content': map_prompt}]
            )

            map_search_parameter = completion.content[0].text
            status.write(f"Using search parameter: {map_search_parameter}")
            
            map_website = app.map_url(url, params={'search': map_search_parameter})
            status.write(f"Found {len(map_website['links'])} links")
            status.update(label="Search completed!", state="complete")
            
            return map_website['links']
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def find_objective_in_top_pages(map_website, objective, app, client):
    try:
        with st.status("Analyzing content...") as status:
            top_links = map_website[:2]
            status.write(f"Analyzing top {len(top_links)} links")
            
            batch_scrape_result = app.batch_scrape_urls(top_links, {'formats': ['markdown']})
            status.write("Content scraped successfully")

            json_pattern = r"\{(?:[^{}]|(?:\{[^{}]*\}))*\}"

            for scrape_result in batch_scrape_result['data']:
                check_prompt = f"""
                Given scraped content and objective, determine if the objective is met.
                Extract relevant information in simple JSON if met.
                Objective: {objective}
                Scraped content: {scrape_result['markdown']}
                """

                completion = client.messages.create(
                    model='claude-3-5-sonnet-20241022',
                    max_tokens=1000,
                    temperature=0,
                    system="Expert web crawler",
                    messages=[{'role': 'user', 'content': check_prompt}]
                )

                result = completion.content[0].text
                json_match = re.search(json_pattern, result, re.DOTALL)
                
                if json_match:
                    try:
                        status.update(label="Analysis completed!", state="complete")
                        return json.loads(json_match.group(0))
                    except json.JSONDecodeError as e:
                        status.write(f"JSON parsing error: {e}")
                        continue

            status.update(label="Analysis completed - No relevant information found", state="complete")
            return None
    except Exception as e:
        st.error(f"Error during analysis: {str(e)}")
        return None

# Process button
if st.button("Extract Information"):
    if not st.session_state.api_keys_set:
        st.error("Please set your API keys first!")
    elif not url or not objective:
        st.error("Please enter both URL and objective!")
    else:
        app, client = initialize_clients()
        map_website = find_relevant_page_via_map(objective, url, app, client)
        
        if map_website:
            result = find_objective_in_top_pages(map_website, objective, app, client)
            if result:
                st.success("Information found!")
                st.json(result)
            else:
                st.warning("No relevant information found for your query.")
        else:
            st.error("Could not map the website. Please check the URL and try again.")

# Footer
st.markdown("---")
st.markdown("Built with Streamlit, Firecrawl, and Anthropic Claude")