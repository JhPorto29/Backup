import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)

# Configuração do MongoDB com variável de ambiente
MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongo:CPgqsJlHBGINDmxqPGVELVxwAzwAvnNf@mongodb.railway.internal:27017")
client = None
db = None
collection = None

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    db = client["meu_banco"]
    collection = db["minha_colecao"]
    client.server_info()  # Verifica a conexão
    print("Conexão com o MongoDB realizada com sucesso!")
except ServerSelectionTimeoutError as e:
    print(f"Erro ao conectar ao MongoDB: {e}")

def handle_error(message, status_code):
    return jsonify({"error": message}), status_code

@app.route('/')
def home():
    return "Servidor funcionando!"

@app.route('/add', methods=['POST'])
def add_data():
    if not collection:
        return handle_error("Banco de dados não configurado corretamente", 500)
    
    data = request.json
    if not data:
        return handle_error("Nenhum dado enviado!", 400)

    try:
        collection.insert_one(data)
        return jsonify({"message": "Dado adicionado com sucesso!"}), 201
    except Exception as e:
        return handle_error(f"Erro ao salvar o dado: {e}", 500)

@app.route('/data', methods=['GET'])
def get_data():
    if not collection:
        return handle_error("Banco de dados não configurado corretamente", 500)

    try:
        data = list(collection.find({}, {"_id": 0}))
        return jsonify(data), 200
    except Exception as e:
        return handle_error(f"Erro ao buscar os dados: {e}", 500)

if __name__ == "__main__":
    app.run(debug=False)  # Não utilizar debug em produção
