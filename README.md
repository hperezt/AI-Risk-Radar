# # AI Risk Radar

## Purpose
AI Risk Radar analyzes project documentation, identifies both obvious and hidden risks, and proposes effective countermeasures. It provides:
- Risk classification by type (cost, timeline, compliance, etc.).
- Intuitive and counterintuitive risk mitigation strategies.
- Risk Matrix (Likelihood × Impact) and an actionable plan.

## Tech Stack
- **Backend**: Python + FastAPI
- **AI Core**: OpenAI GPT-4
- **UI**: Streamlit
- **Deployment**: Render / Hugging Face Spaces

## Features
✔ Upload documents (PDF, DOCX, TXT)  
✔ AI-driven risk detection  
✔ Risk scoring + actionable recommendations  

## Ethical Safeguards
- Transparency: Confidence scores + disclaimers  
- Misuse Prevention: No personal data upload  
- Bias Mitigation: Present options, not absolutes  

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/AI-Risk-Radar.git
cd AI-Risk-Radar
pip install -r requirements.txt
