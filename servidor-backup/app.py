from flask import Flask

# Criação da aplicação Flask
app = Flask(__name__)

# Rota principal
@app.route('/')
def home():
    return "Olá, Mundo!"

# Executando a aplicação (não é necessário para o Gunicorn, mas útil para execução local)
if __name__ == "__main__":
    app.run(debug=True)
