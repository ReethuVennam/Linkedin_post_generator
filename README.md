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
   - Copy or download your generated post.

## How It Works

The application uses **Few-Shot Learning** to generate posts matching your unique writing style:

```
1. UPLOAD POSTS
   └─ You provide LinkedIn post examples (CSV/JSON) or add them manually
   
2. AI LEARNS YOUR STYLE
   └─ Analyzes tone, emoji usage, structure, and vocabulary
   
3. YOU SELECT PARAMETERS
   └─ Choose: Topic + Length + Language
   
4. SMART EXAMPLE SELECTION
   └─ App finds 2 posts matching your criteria
   
5. AI GENERATION
   └─ LLM creates new unique post using your style as reference
   
6. YOU GET RESULT
   └─ Copy to clipboard or download as TXT
```

### Key Technology Features:

- **LangChain 0.3+**: Modern modular architecture for AI workflows
- **Groq Llama 3.3 70B**: Fast, accurate language model (low-latency inference)
- **Few-Shot Learning**: Uses examples to teach AI your writing style
- **Multi-Source Data**: Load from CSV, JSON, or add posts manually
- **Flexible Parameters**: Topic-based, length-controlled, bilingual support

## Data Management

### Supported Data Formats:

**CSV Format:**
```
text,tags,language
"Your post content here","Tag1,Tag2","English"
"Hindi and English mix","Tag1","Hinglish"
```

**JSON Format:**
```json
[
  {
    "text": "Your post content",
    "tags": ["Tag1", "Tag2"],
    "language": "English",
    "line_count": 3
  }
]
```

### How to Use Data Features:

1. **Upload CSV/JSON**: Sidebar → Data Management → Upload tab
2. **Add Posts Manually**: Sidebar → Data Management → Add tab (direct entry)
3. **View Statistics**: Sidebar → Data Management → View tab (see total posts/topics)

The app automatically:
- Validates your data format
- Extracts available topics (tags)
- Categorizes posts by length (Short: 1-5, Medium: 6-10, Long: 11-15 lines)
- Merges data from multiple sources
- Removes duplicate posts

## Architecture

The project consists of these key components:

- **main.py**: Streamlit UI - beautiful interface with data management
- **data_manager.py**: Handles CSV/JSON loading, validation, and storage
- **few_shot.py**: Selects relevant example posts based on criteria
- **post_generator.py**: Builds prompts and calls the LLM
- **llm_helper.py**: Configures Groq LLM with LangChain

## Project Structure

```
linkedin-post-generator/
├── main.py                          # Streamlit UI with data management
├── post_generator.py                # Post generation engine
├── few_shot.py                      # Few-shot learning & example selection
├── data_manager.py                  # CSV/JSON handling (NEW)
├── preprocess.py                    # Data preprocessing utilities
├── llm_helper.py                    # LLM configuration (Groq + LangChain)
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── COMPLETE_PROJECT_EXPLANATION.md # Detailed technical documentation
├── DATA_MANAGEMENT_GUIDE.md        # User guide with examples
├── .env                             # Environment variables (secret - not in repo)
├── add_sample_post.py              # Script to add sample posts
│
├── data/
│   ├── processed_posts.json        # Default example posts
│   ├── custom_posts.json          # User-added posts (auto-created)
│   └── raw_posts.json             # Raw post data
│
└── resources/
    ├── example_posts.csv           # CSV example file
    ├── example_posts.json          # JSON example file
    └── ...
```

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

## Documentation

For detailed information, refer to:

- **[COMPLETE_PROJECT_EXPLANATION.md](COMPLETE_PROJECT_EXPLANATION.md)** - Full technical architecture, data flow, and component details
- **[DATA_MANAGEMENT_GUIDE.md](DATA_MANAGEMENT_GUIDE.md)** - Step-by-step guide for uploading data and adding posts manually

## Quick Start Example

1. **Download example data:**
   ```bash
   cd resources
   # Use example_posts.csv or example_posts.json
   ```

2. **Run the app:**
   ```bash
   streamlit run main.py
   ```

3. **Upload data:**
   - Click sidebar → 📊 Data Management → 📤 Upload
   - Select `resources/example_posts.csv`
   - Click "🚀 Use this data"

4. **Generate posts:**
   - Select Topic: Career
   - Select Length: Medium
   - Select Language: English
   - Click "✨ Generate Post"

5. **Use your post:**
   - Copy to clipboard or download as .txt
   - Share on LinkedIn!

## Features Highlight

### 🎯 Smart Features

| Feature | Benefit |
|---------|---------|
| **Few-Shot Learning** | AI learns your unique writing style |
| **Multi-Source Data** | Load from CSV, JSON, or manual entry |
| **Topic Filtering** | Generate posts only for topics you care about |
| **Length Control** | Short, Medium, or Long posts |
| **Bilingual** | English and Hinglish support |
| **Fast Generation** | Results in seconds using Groq |
| **Beautiful UI** | Modern gradient design with smooth interactions |

## Troubleshooting

**No posts showing up?**
- Make sure you uploaded data or added posts manually
- Check that data format is correct (text, tags, language columns)

**Generation fails?**
- Verify your GROQ_API_KEY is valid in .env
- Check internet connection
- Ensure at least one post exists in the system

**Error reading CSV/JSON?**
- Make sure required columns exist: text, tags, language
- For CSV, tags should be comma-separated: "Career,Tech"
- For JSON, tags should be an array: ["Career", "Tech"]

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/) - Interactive web apps
- Powered by [LangChain](https://langchain.com/) - AI orchestration
- Uses [Groq](https://groq.com/) - Fast AI inference
- Model: Llama 3.3 70B - Open-source language model

## Support

For issues, questions, or suggestions, please [open an issue](https://github.com/ReethuVennam/Linkedin_post_generator/issues) on GitHub.

---

**Made with ❤️ for LinkedIn content creators | v1.0 | Updated March 2026**