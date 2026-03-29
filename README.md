# LinkedIn Post Generator

A Streamlit-based web application that generates engaging LinkedIn posts using AI. Powered by LangChain and Groq, this tool helps create professional content tailored to specific topics, lengths, and languages.

## Features

- **AI-Powered Generation**: Uses advanced language models to create high-quality LinkedIn posts.
- **Customizable Options**: Choose from various topics, post lengths (Short, Medium, Long), and languages (English, Hinglish).
- **Few-Shot Learning**: Incorporates example posts to maintain consistent writing style.
- **User-Friendly Interface**: Simple web interface built with Streamlit.
- **Fast and Efficient**: Quick generation with real-time feedback.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/linkedin-post-generator.git
   cd linkedin-post-generator
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   - Create a `.env` file in the root directory.
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

## Usage

1. **Run the application**:
   ```bash
   streamlit run main.py
   ```

2. **Open your browser** and navigate to the provided URL (usually `http://localhost:8501`).

3. **Generate posts**:
   - Select a topic from the dropdown.
   - Choose the desired length and language.
   - Click "Generate Post" to create your content.

## Requirements

- Python 3.8+
- Groq API key (sign up at [Groq](https://groq.com/))
- Internet connection for API calls

## Dependencies

- streamlit>=1.35.0
- langchain>=0.3.0
- langchain-core>=0.3.0
- langchain-community>=0.3.0
- langchain_groq>=0.1.9
- pandas>=2.2.0
- python-dotenv

## Project Structure

```
linkedin-post-generator/
├── main.py                 # Main Streamlit application
├── post_generator.py       # Post generation logic
├── few_shot.py            # Few-shot learning implementation
├── preprocess.py          # Data preprocessing script
├── llm_helper.py          # LLM configuration
├── requirements.txt       # Python dependencies
├── README.md              # This file
├── .env                   # Environment variables (not in repo)
└── data/
    ├── raw_posts.json     # Raw post data
    └── processed_posts.json # Processed post data
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Make your changes and commit: `git commit -am 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.




