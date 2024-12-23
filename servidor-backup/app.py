from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Obtenha as variáveis de ambiente para a conexão
db_url = os.environ.get('DATABASE_URL')  # Ou use as credenciais específicas

conn = mysql.connector.connect(
    host=db_url.hostname,
    user=db_url.username,
    password=db_url.password,
    database=db_url.database
)
cursor = conn.cursor()

@app.route('/add_data', methods=['POST'])
def add_data():
    data = request.get_json()
    nome = data.get('nome')
    conteudo = data.get('conteudo')

    cursor.execute("INSERT INTO arquivos (nome, conteudo) VALUES (%s, %s)", (nome, conteudo))
    conn.commit()
    return jsonify({"message": "Dados inseridos com sucesso!"}), 201

@app.route('/get_data', methods=['GET'])
def get_data():
    cursor.execute("SELECT * FROM arquivos")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
