import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()

# Obter a URL do banco de dados do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

try:
    # Conectando ao banco de dados
    connection = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = connection.cursor()

    # Teste: exibir a versão do banco de dados
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Conectado ao PostgreSQL: {db_version[0]}")

except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")

finally:
    if 'connection' in locals() and connection:
        cursor.close()
        connection.close()
        print("Conexão com o PostgreSQL encerrada.")
