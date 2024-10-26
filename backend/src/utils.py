import os
from supabase import create_client
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

def get_supabase_client():
    # Leer las variables de entorno
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    # Verificar si las variables existen
    if not url or not key:
        raise ValueError("SUPABASE_URL y SUPABASE_KEY son necesarios.")

    # Crear y devolver el cliente de Supabase
    return create_client(url, key)
