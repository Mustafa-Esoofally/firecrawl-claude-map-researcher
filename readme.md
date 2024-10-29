# Website Information Extractor 🔍

A Streamlit-powered web application that uses Claude AI to intelligently extract specific information from websites. Built with Streamlit, Anthropic's Claude, and Firecrawl.

## Features ✨

- **Intelligent URL Mapping**: Automatically finds relevant pages based on your query
- **Smart Content Extraction**: Uses Claude AI to understand and extract specific information
- **Real-time Status Updates**: Shows progress and results as they happen
- **Structured Output**: Returns information in clean, structured JSON format
- **User-friendly Interface**: Simple, intuitive Streamlit UI
- **Environment Variable Support**: Secure API key management

## Installation 🚀

1. Clone the repository:

```bash
git clone https://github.com/yourusername/website-info-extractor.git
cd website-info-extractor
```


2. Install required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```bash
FIRECRAWL_API_KEY=<your-firecrawl-api-key>
ANTHROPIC_API_KEY=<your-anthropic-api-key>
```


## Usage 💡

1. Start the Streamlit app:

```bash
streamlit run main.py
```


2. Open your browser and navigate to `http://localhost:8501`

3. Enter a website URL and your query

4. View the extracted information in JSON format

## Example Queries 📝

- Find pricing plans
- Extract company contact information
- Locate product features
- Find team member information
- Extract FAQ content

## How It Works 🛠️

1. **URL Mapping**: The application uses Firecrawl to map the website structure and find relevant pages
2. **Content Analysis**: Claude AI analyzes the content to understand context
3. **Information Extraction**: Specific information is extracted based on your query
4. **JSON Formatting**: Results are formatted into clean, structured JSON

## Requirements 📋

- Python 3.8+
- Streamlit
- Anthropic API access
- Firecrawl API access
- python-dotenv

## Environment Variables 🔐

The following environment variables are required:

- `FIRECRAWL_API_KEY`: Your Firecrawl API key
- `ANTHROPIC_API_KEY`: Your Anthropic API key

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [Anthropic](https://www.anthropic.com/) for Claude AI
- [Firecrawl](https://firecrawl.com/) for web crawling capabilities

## Contact 📧

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)

Project Link: [https://github.com/yourusername/website-info-extractor](https://github.com/yourusername/website-info-extractor)
