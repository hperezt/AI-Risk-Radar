import os
import json
import openai

# Configurar la API Key desde variable de entorno
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_risks(text: str, context: str = "") -> dict:
    """
    Genera 10 riesgos (5 intuitivos y 5 contraintuitivos) para proyectos ferroviarios
    usando GPT-4. Devuelve un diccionario con riesgos, justificación y contramedidas.
    """

    # Construir el prompt
    prompt = f"""
    Actúa como un analista experto en gestión de riesgos para proyectos de infraestructura ferroviaria.

    Instrucciones:
    - Analiza el siguiente texto del proyecto.
    - Considera este contexto adicional: {context}
    - Devuelve EXACTAMENTE este formato en JSON:
    {{
      "intuitive_risks": [
        {{"risk": "", "justification": "", "countermeasure": ""}}
      ],
      "counterintuitive_risks": [
        {{"risk": "", "justification": "", "countermeasure": ""}}
      ]
    }}

    - Incluye 5 riesgos intuitivos (obvios).
    - Incluye 5 riesgos contraintuitivos (ocultos o sistémicos).
    - Cada riesgo debe tener:
      - "risk": título breve del riesgo
      - "justification": explicación corta
      - "countermeasure": medida creativa para mitigarlo

    Texto del proyecto:
    {text}
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un experto en análisis de riesgos."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6
        )

        # Extraer respuesta de GPT
        content = response['choices'][0]['message']['content']

        # Intentar parsear el JSON
        risks_data = json.loads(content)

        return risks_data

    except Exception as e:
        return {"error": str(e)}
