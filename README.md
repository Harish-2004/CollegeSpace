# 🤖 AI Agent Resume Builder

An intelligent resume builder powered by AI agents that creates professional, ATS-optimized resumes and cover letters using multiple LLM options including FREE alternatives.

## ✨ Features

- **🤖 AI Agents**: Multiple specialized agents for different resume building tasks
- **📊 Database Integration**: MongoDB support for user data management
- **📄 LaTeX Generation**: Professional PDF resume output
- **🎯 ATS Optimization**: Applicant Tracking System optimization
- **📝 Cover Letters**: AI-generated personalized cover letters
- **🔍 Skill Analysis**: Gap analysis and skill matching
- **🆓 Multiple LLM Options**: Support for free and paid LLM services
- **⚡ CrewAI Framework**: Advanced multi-agent orchestration

## 🏗️ Architecture

### AI Agents
- **Database Manager**: Handles user data retrieval and validation
- **Profile Analyzer**: Analyzes user data and job requirements
- **Resume Writer**: Creates ATS-optimized resume content
- **Cover Letter Specialist**: Generates personalized cover letters
- **Skill Gap Analyst**: Identifies skill gaps and recommendations
- **ATS Optimization Specialist**: Optimizes for Applicant Tracking Systems

### LLM Support
- **Google Gemini** (Recommended) - Professional quality
- **Hugging Face** (FREE) - Multiple free models available
- **Local Ollama** (FREE) - Run models locally
- **Mock LLM** (FREE) - For testing and development

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- MongoDB (local or cloud)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-agent-resume-builder.git
   cd ai-agent-resume-builder
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Set up database**
   ```bash
   python setup_database.py
   ```

6. **Run the resume builder**
   ```bash
   python main.py
   ```

## ⚙️ Configuration

### Environment Variables (.env)

```env
# LLM Configuration (choose one or more)
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here

# Database Configuration
MONGODB_URI=mongodb://localhost:27017/

# Application Configuration
USER_ID=demo_user_id
JOB_PROFILE=Software Engineer at TechCorp, focusing on backend development, Python, and cloud infrastructure.
CREW_TYPE=full
```

### LLM Options

#### 🎯 Google Gemini (Recommended)
- **Cost**: Low cost, excellent value
- **Quality**: EXCELLENT for resume building
- **Setup**: Get API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

#### 🆓 FREE Options

**Hugging Face (FREE tier available)**
- **Cost**: $0 (completely free)
- **Models**: DeepSeek-V3, DialoGPT, GPT-2, GPT-Neo
- **Setup**: Get FREE token from [Hugging Face](https://huggingface.co/settings/tokens)

**Local Ollama (FREE - if you have enough RAM)**
- **Cost**: $0 (runs on your computer)
- **Models**: Mistral, Llama2, CodeLlama
- **Setup**: Install from [Ollama](https://ollama.ai/download)

**Mock LLM (FREE - for testing)**
- **Cost**: $0 (instant responses)
- **Use**: Automatic fallback for testing

## 📖 Usage

### Basic Usage

```python
from main import run_resume_builder

# Run full resume builder
result = run_resume_builder(
    user_id="demo_user_id",
    job_profile="Software Engineer at TechCorp, focusing on backend development, Python, and cloud infrastructure.",
    crew_type="full"
)
```

### Different Crew Types

```python
# Full resume builder (default)
result = run_resume_builder(user_id="user_1", job_profile="...", crew_type="full")

# Skill analysis only
result = run_resume_builder(user_id="user_1", job_profile="...", crew_type="skill_analysis")

# ATS optimization only
result = run_resume_builder(user_id="user_1", job_profile="...", crew_type="ats_optimization")
```

### Database Operations

```python
from agents.data_collector import collect_user_data, validate_job_profile

# Collect user data
user_data = collect_user_data("user_id")

# Validate job profile
job_data = validate_job_profile("Software Engineer position...")
```

## 📊 Sample Data

The project includes comprehensive sample user data:

- **John Doe**: Senior Software Engineer with 5+ years experience
- **Sarah Johnson**: Frontend Developer with React expertise

Sample data includes:
- Professional experience
- Education and certifications
- Skills and technologies
- Projects and achievements
- Social links and interests

## 🎯 Features in Detail

### Resume Generation
- **Professional formatting** using LaTeX templates
- **ATS optimization** with keyword matching
- **Customizable sections** (experience, education, skills, projects)
- **PDF output** for easy sharing

### Cover Letter Generation
- **Personalized content** based on job requirements
- **Professional tone** with persuasive writing
- **Skill matching** to job description
- **Storytelling approach** to connect experience

### Skill Analysis
- **Gap identification** between user skills and job requirements
- **Learning recommendations** for skill development
- **Transferable skills** identification
- **Career path suggestions**

### ATS Optimization
- **Keyword optimization** for maximum visibility
- **Format compliance** with ATS requirements
- **Content structure** optimization
- **Screening algorithm** compatibility

## 🔧 Development

### Project Structure
```
AI_AGENT_RESUME_BUILDER/
├── agents/                 # AI agents and crew definitions
│   ├── crew_agents.py     # Agent definitions
│   ├── crew_crew.py       # Crew orchestration
│   ├── crew_tasks.py      # Task definitions
│   ├── data_collector.py  # Database operations
│   ├── latex_generator.py # LaTeX template generation
│   └── compiler.py        # PDF compilation
├── config/                # Configuration files
│   ├── llm_config.py     # LLM configuration
│   └── mcp_config.py     # MCP configuration
├── templates/             # LaTeX templates
│   ├── resume_template.tex
│   ├── cover_letter_template.tex
│   └── skill_report_template.tex
├── main.py               # Main application entry point
├── setup_database.py     # Database setup script
└── requirements.txt      # Python dependencies
```

### Adding New Agents

```python
from crewai import Agent

new_agent = Agent(
    role="Your Agent Role",
    goal="Your agent's goal",
    backstory="Your agent's backstory",
    verbose=True,
    llm=llm
)
```

### Adding New LLM Providers

```python
def get_custom_llm():
    return LLM(
        model="your_model_name",
        api_key=os.getenv("YOUR_API_KEY"),
        base_url="your_base_url",
        temperature=0.7
    )
```

## 🧪 Testing

### Test LLM Configuration
```bash
python test_cloud_api.py
```

### Test Database Connection
```bash
python check_database.py
```

### Run with Sample Data
```bash
python main.py
```

## 📈 Performance

### LLM Performance Comparison

| Provider | Writing Quality | Analysis | Speed | Cost | Best For |
|----------|----------------|----------|-------|------|----------|
| Google Gemini | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | Low | Professional resumes |
| Hugging Face | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | FREE | General use |
| Local Ollama | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | FREE | Privacy-focused |
| Mock LLM | ⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | FREE | Testing |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include tests for new features
- Update documentation for changes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent framework
- [Hugging Face](https://huggingface.co/) - Free LLM models
- [Ollama](https://ollama.ai/) - Local LLM deployment
- [Google AI](https://ai.google.dev/) - Gemini API

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/ai-agent-resume-builder/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/ai-agent-resume-builder/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/ai-agent-resume-builder/wiki)

## 🚀 Roadmap

- [ ] Web interface for easier usage
- [ ] More LLM provider integrations
- [ ] Advanced ATS optimization algorithms
- [ ] Resume template customization
- [ ] Multi-language support
- [ ] Real-time collaboration features

---

⭐ **Star this repository if you find it helpful!** 