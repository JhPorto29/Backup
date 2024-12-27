from dotenv import load_dotenv
import os
import psycopg2

# Carregar variáveis de ambiente
load_dotenv()

# Obter URL do banco de dados
DATABASE_URL = os.getenv('DATABASE_URL')

# Conectar ao banco de dados
conn = psycopg2.connect(DATABASE_URL, sslmode='require')

# Executar comandos SQL
cur = conn.cursor()
cur.execute("SELECT * FROM tabela;")
rows = cur.fetchall()
print(rows)

# Fechar a conexão
cur.close()
conn.close()
