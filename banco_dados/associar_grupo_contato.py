from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

selecionar_grupo = 'SELECT id FROM grupos WHERE descrição = %s'
atualizar_contato = 'UPDATE contatos SET grupo_id = %s WHERE nome = %s'

contato_grupo = {
    '...': 'Casa', 
    '...': 'Trabalho',

    'Ana': 'Casa',
    'Bia': 'Trabalho',
    'Lucas Yuri': 'Casa',
    'Lu': 'Trabalho',
    'Gui': 'Casa',
    'Beca': 'Trabalho',
    'Pedro': 'Casa',
    'Luca': 'Trabalho',
}

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(selecionar_grupo, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(atualizar_contato, (grupo_id, contato))
            conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
        print('Contatos associados')
        