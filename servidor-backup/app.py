import os
import mysql.connector
from flask import Flask

app = Flask(__name__)

# Carregar a variável de ambiente
db_url = os.environ.get('DATABASE_URL')

if not db_url:
    raise ValueError("A variável de ambiente DATABASE_URL não está configurada!")

# Conectar ao banco de dados
try:
    conn = mysql.connector.connect(
        host=db_url.hostname,
        user=db_url.username,
        password=db_url.password,
        database=db_url.database
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Erro ao conectar ao banco de dados: {err}")
    raise

@app.route('/')
def index():
    return "Servidor rodando com banco de dados configurado!"

if __name__ == '__main__':
    app.run(debug=True)
