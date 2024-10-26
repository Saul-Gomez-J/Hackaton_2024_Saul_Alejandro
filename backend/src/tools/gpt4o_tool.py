import os
import openai

class GPT4oTool:
    def __init__(self):
        self.api_key = os.getenv("GPT4O_API_KEY")
        openai.api_key = self.api_key
        self.name = "GPT4oTool"
        self.description = "Genera respuestas utilizando el modelo GPT-4o-mini para consultas generales."
        self.model_fields = {
            "prompt": "El mensaje o pregunta a la que se quiere obtener una respuesta."
        }

    def generate_response(self, prompt: str) -> str:
        # Resto del código...

        try:
            response = openai.Completion.create(
                model="gpt-4o-mini",  # Modelo específico
                prompt=prompt,
                max_tokens=200  # Ajuste según necesidad
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error al generar respuesta con GPT-4o-mini: {e}"
