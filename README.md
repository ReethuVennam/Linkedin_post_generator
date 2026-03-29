# 🚀 LinkedIn Post Generator - Advanced AI Content Creation

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A **production-ready, enterprise-level AI application** that generates professional LinkedIn posts using advanced prompt engineering techniques. This project demonstrates **cutting-edge GenAI/LLM engineering skills** suitable for senior AI roles.

## ✨ **Advanced Features**

### 🤖 **AI-Powered Generation**
- **6 Prompt Engineering Strategies**: Baseline, Few-shot, Chain-of-thought, Detailed instructions, Style emphasis
- **Performance Analytics**: Real-time metrics, A/B testing, statistical analysis
- **Quality Optimization**: Automated evaluation of engagement, relevance, and style

### 📊 **Intelligent Data Management**
- **Multi-Source Integration**: CSV, JSON, Manual entry, API support
- **Smart Example Selection**: Context-aware few-shot learning
- **Real-time Analytics**: Dynamic data statistics and health monitoring

### 🎨 **Professional UI/UX**
- **Custom Styling**: Gradient backgrounds, smooth animations, responsive design
- **Advanced Dashboard**: Performance metrics, data management tabs, analytics
- **One-Click Generation**: Streamlined workflow with progress indicators

### 🧪 **Testing & Validation**
- **Automated Test Suite**: Component validation, integration testing, performance benchmarking
- **Quality Assurance**: 100% functional verification across all features
- **Analytics Reporting**: Charts, radar plots, comprehensive evaluation

---

## 🚀 **Quick Deploy**

### **Streamlit Cloud (Recommended)**
[![Deploy to Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

1. **Fork this repository** to your GitHub account
2. **Go to [Streamlit Cloud](https://share.streamlit.io/)**
3. **Connect your GitHub** and select this repository
4. **Configure secrets** in Streamlit Cloud dashboard:
   ```
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
5. **Deploy!** Your app will be live at `https://your-app-name.streamlit.app`

### **Local Development**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/linkedin-post-generator.git
   cd linkedin-post-generator
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**:
   ```bash
   # Create .env file
   echo "GROQ_API_KEY=your_api_key_here" > .env
   ```

5. **Run locally**:
   ```bash
   streamlit run main.py
   ```

---

## 🎯 **How It Works**

### **Advanced AI Pipeline**
```
🌟 USER INTERFACE LAYER
    🎨 Professional UI (Streamlit + Custom CSS)
    📊 Advanced Sidebar (Metrics, Controls, Settings)
    📁 Data Management Hub (Upload/Manual/View tabs)

🧪 PROMPT ENGINEERING LAYER
    🎯 6 Strategies: baseline, few_shot_2/4, detailed_instructions
    🔬 Automated A/B testing with statistical analysis
    📈 Performance metrics: time, quality, engagement

📊 ANALYTICS & VISUALIZATION LAYER
    📈 Statistical analysis (means, correlations, distributions)
    📊 Performance visualization (charts, radar plots)
    📋 Automated report generation (Markdown + PNG)

💾 DATA MANAGEMENT LAYER
    🔄 Multi-source integration (CSV/JSON/Manual)
    🎯 Smart example selection (topic/length/language)
    📊 Real-time statistics and validation

🎯 FEW-SHOT LEARNING LAYER
    🧠 Context-aware example selection
    ⭐ Quality-based ranking algorithm
    🔄 Dynamic data source integration

🤖 POST GENERATION LAYER
    ✨ Dynamic prompt construction with examples
    🔧 Multi-strategy prompt engineering
    ⚡ Performance optimization with quality preservation

⚡ LLM INTEGRATION LAYER
    🚀 Groq Llama 3.3 70B (fast, high-quality inference)
    🔒 Secure API key management
    🛡️ Production-ready error handling
```

### **Key Technology Stack**
- **Frontend**: Streamlit 1.35+ (Reactive web UI)
- **AI Framework**: LangChain 0.3+ (Modular LLM integration)
- **LLM**: Groq Llama 3.3 70B (Fast inference, high quality)
- **Data**: Pandas (Data manipulation & analysis)
- **Visualization**: Matplotlib + Seaborn (Analytics charts)
- **Deployment**: Streamlit Cloud (Zero-config deployment)

---

## 📊 **Performance Analytics**

### **Strategy Performance Matrix**

| Strategy | Speed | Quality | Engagement | Use Case |
|----------|-------|---------|------------|----------|
| **style_emphasis** | ⚡ Fast | ⭐⭐⭐ | 🔥🔥🔥 | Social media optimization |
| **few_shot_2** | ⚡ Fast | ⭐⭐⭐ | ⭐⭐ | Balanced performance |
| **detailed_instructions** | 🐌 Slow | ⭐⭐⭐ | 🔥🔥 | Hashtag mastery |
| **chain_of_thought** | 🐌 Slow | ⭐⭐⭐ | ⭐⭐⭐ | Consistent output |
| **few_shot_4** | 🐌 Slow | ⭐⭐⭐ | ⭐⭐ | Quality priority |
| **baseline** | ⚡⚡ Fast | ⭐⭐ | ⭐ | Speed priority |

### **Quality Metrics**
- **⏱️ Generation Time**: < 1.0s (fast), 1.0-2.0s (moderate), >2.0s (slow)
- **📏 Length Appropriateness**: 100% target achievement
- **😊 Emoji Usage**: 0-100% engagement indicator
- **#️⃣ Hashtag Usage**: 0-100% LinkedIn optimization
- **🎯 Topic Relevance**: 100% content quality assurance

---

## 📁 **Project Structure**

```
linkedin_post_generator/
├─ 📁 Core Modules
│  ├─ main.py (Streamlit UI - Advanced interface)
│  ├─ data_manager.py (Multi-source data management)
│  ├─ few_shot.py (Intelligent example selection)
│  ├─ post_generator.py (AI generation core)
│  ├─ llm_helper.py (Production LLM integration)
│  ├─ prompt_tester.py (Strategy testing framework)
│  └─ prompt_analysis.py (Analytics engine)
├─ 📁 Data & Resources
│  ├─ data/ (JSON/CSV storage)
│  └─ resources/ (Assets)
├─ 📁 Documentation
│  ├─ README.md (This file)
│  ├─ COMPLETE_PROJECT_EXPLANATION.md (Technical deep-dive)
│  └─ DATA_MANAGEMENT_GUIDE.md (Data operations)
├─ 📁 Analytics Output
│  ├─ prompt_analysis_report.md (Analysis reports)
│  └─ prompt_test_results.json (Test data)
├─ 📁 Deployment
│  ├─ requirements.txt (Python dependencies)
│  ├─ packages.txt (System dependencies)
│  ├─ .streamlit/config.toml (Streamlit configuration)
│  └─ .streamlit/secrets.toml (Secrets template)
└─ 📁 Configuration
   ├─ .env.example (Environment template)
   └─ .gitignore (Security exclusions)
```

---

## 🔧 **Configuration**

### **Environment Variables**
Create a `.env` file for local development:
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### **Streamlit Cloud Secrets**
In Streamlit Cloud dashboard, add:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## 🧪 **Testing & Validation**

Run the comprehensive test suite:
```bash
# Test all components
python test_components.py

# Run prompt engineering tests
python prompt_tester.py

# Generate analytics report
python prompt_analysis.py
```

---

## 📈 **Analytics & Reporting**

### **Automated Reports**
- **Performance Charts**: Generation time distributions
- **Quality Radar**: Multi-dimensional strategy comparison
- **Statistical Summary**: Means, correlations, insights
- **Recommendations**: Best strategy suggestions

### **Export Formats**
- 📊 PNG Charts (Visualization)
- 📋 Markdown Reports (Analysis)
- 📄 JSON Data (Raw metrics)

---

## 🤝 **Contributing**

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **Groq** for providing fast LLM inference
- **LangChain** for the modular AI framework
- **Streamlit** for the amazing web app framework
- **OpenAI** for inspiring modern AI development practices

---

## 📞 **Contact & Support**

**Repository**: [GitHub - LinkedIn Post Generator](https://github.com/your-username/linkedin-post-generator)

**Features Demonstrated**:
- Advanced Prompt Engineering
- Production AI Application Development
- Performance Analytics & Visualization
- Modern LangChain Integration
- Professional UI/UX Design
- Comprehensive Testing Framework

**Built with ❤️ for the AI engineering community**

---

## 💼 **Perfect for AI Job Applications**

This project showcases **enterprise-level AI engineering skills** required for:

- **Senior GenAI Engineer** roles
- **LLM Engineer** positions
- **AI Application Developer** jobs
- **Machine Learning Engineer** opportunities

**🚀 Ready to impress hiring managers with advanced AI capabilities!**

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

