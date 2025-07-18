# AI Risk Radar

## Purpose
AI Risk Radar analyzes project documentation, identifies both obvious and hidden risks, and proposes effective countermeasures.

## Tech Stack
- Backend: Python + FastAPI
- AI Core: OpenAI GPT-4
- UI: Streamlit
- Deployment: Render / Hugging Face Spaces

## Features
✔ Upload documents (PDF, DOCX, TXT)  
✔ AI-driven risk detection  
✔ Risk scoring + actionable recommendations  

## Installation
```bash
git clone git@github.com:hperezt/AI-Risk-Radar.git
cd AI-Risk-Radar
pip install -r requirements.txt
```

## Run the App
```bash
streamlit run ui/streamlit_app.py
```

## Ethical Safeguards
- Transparency: Confidence scores + disclaimers  
- Misuse Prevention: No personal data upload  
- Bias Mitigation: Present options, not absolutes  

