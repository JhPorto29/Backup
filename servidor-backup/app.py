from flask import Flask, jsonify, request

# Criando a instância do servidor Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return 'Servidor Backup está rodando!'

# Rota para criar um usuário (POST)
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()  # Obtém os dados enviados no corpo da requisição (JSON)
    
    name = data.get('name')
    email = data.get('email')

    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400

    return jsonify({
        "message": "Usuário criado com sucesso!",
        "user": {
            "name": name,
            "email": email
        }
    }), 201

# Iniciando o servidor na porta 5000
if __name__ == '__main__':
    app.run(debug=True, port=5000)
