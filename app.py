from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import sql

# Carregar variáveis de ambiente
load_dotenv()

# Obter URL do banco de dados a partir da variável de ambiente
DATABASE_URL = os.getenv('DATABASE_URL')

# Verificar se a variável de ambiente foi carregada corretamente
if DATABASE_URL is None:
    raise ValueError("A variável de ambiente DATABASE_URL não está configurada.")

try:
    # Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')

    # Criar um cursor
    cur = conn.cursor()

    # Executar uma consulta SQL segura
    query = sql.SQL("SELECT * FROM {}").format(sql.Identifier('tabela'))  # Substitua 'tabela' pelo nome real da tabela
    cur.execute(query)

    # Obter os resultados
    rows = cur.fetchall()
    print(rows)

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

finally:
    # Fechar o cursor e a conexão
    if cur:
        cur.close()
    if conn:
        conn.close()
