from flask import Flask, jsonify
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do arquivo .env

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

# Conexão com o banco de dados
try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    print("Conexão com o banco de dados estabelecida com sucesso!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
    conn = None

@app.route("/")
def index():
    if conn:
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        return jsonify({"message": "Servidor conectado ao banco de dados!", "db_version": db_version[0]})
    return jsonify({"error": "Banco de dados não conectado"}), 500

if __name__ == "__main__":
    app.run(debug=True)
