import os
from anthropic import Anthropic

class ClaudeTool:
    def __init__(self):
        self.api_key = os.getenv("CLAUDE_API_KEY")
        self.client = Anthropic(api_key=self.api_key)
        self.name = "ClaudeTool"
        self.description = "Genera respuestas utilizando el modelo Claude Haiku para consultas generales."
        self.model_fields = {
            "prompt": "El mensaje o pregunta a la que se quiere obtener una respuesta."
        }

    def generate_response(self, prompt: str) -> str:
        # Resto del código...

        try:
            response = self.client.completions.create(
                model="claude-haiku",
                prompt=prompt,
                max_tokens=200
            )
            return response.completion.strip()
        except Exception as e:
            return f"Error al generar respuesta con Claude Haiku: {e}"
