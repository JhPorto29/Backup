from flask import Flask, jsonify
import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)

# Carregar a URL do banco de dados
DATABASE_URL = os.getenv("DATABASE_URL")

# Verificar se a variável DATABASE_URL foi carregada corretamente
if not DATABASE_URL:
    raise ValueError("A variável de ambiente 'DATABASE_URL' não foi definida.")

# Função para conectar ao banco de dados
def connect_db():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except Exception as e:
        app.logger.error(f"Erro ao conectar ao banco de dados: {e}")
        return None

# Rota principal
@app.route("/")
def index():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(sql.SQL("SELECT version();"))
            db_version = cursor.fetchone()
            return jsonify({"message": "Servidor conectado ao banco de dados!", "db_version": db_version[0]})
        except Exception as e:
            app.logger.error(f"Erro ao executar consulta no banco de dados: {e}")
            return jsonify({"error": "Erro ao consultar o banco de dados"}), 500
        finally:
            # Garantir que a conexão seja fechada
            conn.close()
    else:
        return jsonify({"error": "Banco de dados não conectado"}), 500

if __name__ == "__main__":
    # Configuração para rodar localmente
    app.run(host="0.0.0.0", port=5000, debug=True)
