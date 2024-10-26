import os
import openai  

class GPT4oTool:
    def __init__(self):
        # Obtenemos el API key de las variables de entorno
        self.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key

    def generate_response(self, prompt: str) -> str:
        try:
            # Llamada al modelo GPT-4o-mini mediante OpenAI
            response = openai.Completion.create(
                model="gpt-4o-mini",  # Especificamos el modelo
                prompt=prompt,
                max_tokens=200  # Ajusta el límite de tokens según sea necesario
            )
            # Devolvemos el texto generado
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error al generar respuesta con GPT-4o-mini: {e}"
