# 🏥 Clinisight AI - Medical Diagnosis Assistant

An AI-powered medical diagnosis system that combines GPT-4's language understanding with real-time PubMed research integration to provide intelligent symptom analysis and medical insights.

## ✨ Features

- 🔍 **Intelligent Symptom Extraction**: Uses GPT-4 to identify medical symptoms from natural language
- 💊 **AI-Powered Diagnosis**: Generates possible diagnoses based on extracted symptoms
- 📚 **PubMed Integration**: Automatically retrieves relevant medical research
- 📝 **Research Summarization**: Summarizes complex medical literature
- 🔌 **MCP Support**: Model Context Protocol integration for AI agents
- 🚀 **FastAPI Backend**: High-performance REST API
- ⚡ **Error Handling**: Comprehensive error handling and logging

## 🛠️ Installation

### Prerequisites
- Python 3.11 or higher
- OpenAI API key

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/codedbydimpal/MedicalDiagnosisapp.git
cd MedicalDiagnosisapp
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

4. **Configure environment variables**

Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 🚀 Usage

### Running the FastAPI Server

```bash
# Development mode with auto-reload
uvicorn app:app --reload --port 8080

# Production mode
uvicorn app:app --host 0.0.0.0 --port 8080
```

The API will be available at: `http://localhost:8080`
- API Documentation: `http://localhost:8080/docs`
- Alternative docs: `http://localhost:8080/redoc`

### API Endpoints

#### POST /diagnosis
Analyze symptoms and get diagnosis with research.

**Request:**
```bash
curl -X POST http://localhost:8080/diagnosis \
  -H "Content-Type: application/json" \
  -d '{
    "description": "I have been experiencing severe headache, high fever, and fatigue for the past two days"
  }'
```

**Response:**
```json
{
  "symptoms": ["severe headache", "high fever", "fatigue"],
  "diagnosis": "Based on the symptoms...",
  "pubmed_summary": "Recent research indicates...",
  "articles_count": 3
}
```

#### GET /health
Health check endpoint.

```bash
curl http://localhost:8080/health
```

### Running the MCP Server

```bash
# Development mode
uv run mcp dev mcp_tool.py

# Install as MCP tool
mcp install mcp_tool.py
```

## 📁 Project Structure

```
MedicalDiagnosisapp/
├── app.py                          # FastAPI application
├── mcp_tool.py                     # MCP server implementation
├── config.py                       # Configuration and env validation
├── main.py                         # Entry point
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project metadata
├── .env                            # Environment variables (create this)
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
├── functions/
│   ├── __init__.py
│   ├── symptom_extractor.py       # AI-powered symptom extraction
│   ├── diagnosis_symptoms.py      # Diagnosis generation
│   ├── pubmed_articles.py         # PubMed API integration
│   └── summarize_pubmed.py        # Research summarization
└── demo.ipynb                      # Jupyter notebook demo
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | OpenAI API key for GPT-4 access | Yes |

### Model Configuration

The application uses GPT-4 by default. You can modify the model in the respective function files:
- `functions/symptom_extractor.py`
- `functions/diagnosis_symptoms.py`
- `functions/summarize_pubmed.py`

## 🧪 Testing

```bash
# Test the symptom extraction
python -c "from functions.symptom_extractor import extract_symptoms; print(extract_symptoms('I have a headache and fever'))"

# Test the API endpoint
curl -X POST http://localhost:8080/diagnosis \
  -H "Content-Type: application/json" \
  -d '{"description": "headache and fever"}'
```

## 📊 Logging

Logs are written to:
- Console (stdout)
- `app.log` file

Log format: `TIMESTAMP - LOGGER_NAME - LEVEL - MESSAGE`

## ⚠️ Important Disclaimers

1. **Not for Medical Advice**: This tool is for educational and research purposes only
2. **Consult Professionals**: Always consult qualified healthcare professionals for medical advice
3. **No Liability**: The developers assume no responsibility for medical decisions made based on this tool
4. **Research Tool**: Intended to assist in medical research and education, not diagnosis

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📝 License

This project is for educational purposes. Please ensure compliance with:
- OpenAI's usage policies
- PubMed's terms of service
- Applicable medical data regulations

## 🐛 Troubleshooting

### Common Issues

**Issue**: `OPENAI_API_KEY not set`
- **Solution**: Create a `.env` file with your OpenAI API key

**Issue**: Import errors
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

**Issue**: Port already in use
- **Solution**: Change the port: `uvicorn app:app --port 8081`

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🙏 Acknowledgments

- OpenAI for GPT-4 API
- NCBI for PubMed access
- FastAPI framework
- Model Context Protocol (MCP)
