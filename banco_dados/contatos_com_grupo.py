from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = """
    SELECT
        grupos.descrição AS grupo,
        contatos.nome As nome
    FROM contatos
    INNER JOIN grupos ON contatos.grupos_id = grupos.id
    ORDER BY grupo, nome
"""

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["nome"]}')

