from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
import tempfile
import shutil

from app.parsers import extract_text_from_pdf, extract_text_from_txt
from app.risk_engine import generate_risks

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Risk Radar API is running"}

@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...), context: str = Form("")):
    try:
        # Guardar archivo temporalmente
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        # Extraer texto según el tipo
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(tmp_path)
        elif file.filename.endswith(".txt"):
            text = extract_text_from_txt(tmp_path)
        else:
            return JSONResponse(content={"error": "Formato no soportado"}, status_code=400)

        # Llamar a la lógica de riesgos
        risks = generate_risks(text, context)

        return JSONResponse(content=risks)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
