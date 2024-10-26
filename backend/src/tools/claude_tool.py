import os
import anthropic  # Importamos la librería Anthropic
from dotenv import load_dotenv  # Importamos dotenv para cargar el archivo .env

# Cargar las variables de entorno desde .env
load_dotenv()

class ClaudeTool:
    def __init__(self):
        # Obtenemos la clave de API desde el entorno
        self.api_key = os.getenv("CLAUDE_API_KEY")
        os.environ["ANTHROPIC_API_KEY"] = self.api_key  # Establecemos la API key en el entorno
        self.client = anthropic.Client()  # Instanciamos el cliente sin argumentos adicionales

    def generate_response(self, prompt: str) -> str:
        try:
            # Llamada al modelo Claude Haiku mediante Anthropic
            response = self.client.completions.create(
                model="claude-haiku",  # Especificamos el modelo
                prompt=prompt,
                max_tokens=200  # Ajusta el límite de tokens según sea necesario
            )
            # Devolvemos el texto generado
            return response.completion.strip()
        except Exception as e:
            return f"Error al generar respuesta con Claude Haiku: {e}"
