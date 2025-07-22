def extract_text_from_pdf(file_path: str) -> str:
    """
    Simple placeholder for PDF extraction using PyPDF2.
    """
    return "Simulated extracted text from PDF."

def extract_text_from_txt(file_path: str) -> str:
    """
    Reads plain text file content.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
