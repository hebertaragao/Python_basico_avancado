from bd import nova_conexao
from mysql.connector import ProgrammingError

tabela_contatos = """
    CREATE TABLE contatos(nome VARCHAR(50), tel VARCHAR(40))

"""

tablea_emails = """
    CREATE TABLE emails(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        dono VARCHAR(50)
    )
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(tabela_contatos)
        cursor.execute(tablea_emails)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
        