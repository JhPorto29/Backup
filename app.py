from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

app = Flask(__name__)

# Carregar a URL do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

# Verificar se a variável DATABASE_URL foi carregada corretamente
if not DATABASE_URL:
    raise ValueError("DATABASE_URL não definida no arquivo .env")

# Conexão com o banco de dados
def connect_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Conexão inicial
conn = connect_db()
cursor = conn.cursor() if conn else None

@app.route("/")
def index():
    if conn:
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        return jsonify({"message": "Servidor conectado ao banco de dados!", "db_version": db_version[0]})
    return jsonify({"error": "Banco de dados não conectado"}), 500

if __name__ == "__main__":
    # Rodar o servidor em produção com Gunicorn (para quando em produção)
    app.run(debug=True)
