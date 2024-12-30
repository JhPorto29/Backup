from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)

# Configuração do MongoDB
try:
    client = MongoClient("mongodb://mongo:CPgqsJlHBGINDmxqPGVELVxwAzwAvnNf@mongodb.railway.internal:27017", serverSelectionTimeoutMS=5000)
    db = client["meu_banco"]  # Nome do banco de dados
    collection = db["minha_colecao"]  # Nome da coleção
    # Testa a conexão com o servidor
    client.server_info()  # Lança um erro se a conexão falhar
    print("Conexão com o MongoDB realizada com sucesso!")
except ServerSelectionTimeoutError as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    db = None
    collection = None

@app.route('/')
def home():
    return "Servidor funcionando!"

@app.route('/add', methods=['POST'])
def add_data():
    if not collection:
        return jsonify({"error": "Banco de dados não configurado corretamente"}), 500
    
    data = request.json
    if not data:
        return jsonify({"error": "Nenhum dado enviado!"}), 400

    try:
        collection.insert_one(data)
        return jsonify({"message": "Dado adicionado com sucesso!"}), 201
    except Exception as e:
        return jsonify({"error": f"Erro ao salvar o dado: {e}"}), 500

@app.route('/data', methods=['GET'])
def get_data():
    if not collection:
        return jsonify({"error": "Banco de dados não configurado corretamente"}), 500

    try:
        data = list(collection.find({}, {"_id": 0}))  # Ignora o campo "_id" ao retornar os dados
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": f"Erro ao buscar os dados: {e}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
