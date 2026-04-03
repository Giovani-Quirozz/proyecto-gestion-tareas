import os
import psycopg2
from dotenv import load_dotenv

# Esto lee tu archivo .env
load_dotenv()

def obtener_conexion():
    try:
        url = os.getenv("DATABASE_URL")
        # Conexión a la nube
        conn = psycopg2.connect(url)
        print("✅ ¡Conexión exitosa a Supabase!")
        return conn
    except Exception as e:
        print(f"❌ Error al conectar: {e}")
        return None

if __name__ == "__main__":
    obtener_conexion()