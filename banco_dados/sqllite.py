from sqlite3 import connect, ProgrammingError, Row

tabela_grupo = """
    CREATE TABLE IF NOT EXISTS grupos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descrição VARCHAR(30)
    )
"""
tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nome VARCHAR(50),
        tel VARCHAR(40),
        grupo_id INTEGER,
        FOREIGN KEY (grupo_id) REFERENCES grupos(id)
        )
"""
insert_grupos = 'INSERT INTO grupos (descrição) VALUES (?)'
select_grupos = 'SELECT id, descrição FROM grupos'
insert_contatos = 'INSERT INTO contatos (nome, tel, grupo_id) VALUES (?, ?, ?)'
select = """
    SELECT grupos.descrição As grupo, contatos.nome AS contato
    FROM contatos
    INNER JOIN  grupos ON contatos.grupo_id = grupos.id
    ORDER BY grupo, contato
"""
try:
    conexao = connect(':memory:')
    conexao.row_factory = Row
    cursor = conexao.cursor()

    cursor.execute(tabela_grupo)
    cursor.execute(tabela_contatos)

    cursor.executemany(insert_grupos, (('Casa',), ('Trabalho',)))
    cursor.execute(select_grupos)
    grupos = {row['descrição']: row['id'] for row in cursor.fetchall()}

    contatos = (
        ('Arthur', '456', grupos['Casa']),
        ('Paulo', '789', grupos['Casa']),
        ('Ângelo', '000', grupos['Trabalho']),
        ('Eduardo', '987', None),
        ('Yuri', '654', None),
        ('Leonardo', '321', None),
    )
    cursor.executemany(insert_contatos, contatos)

    cursor.execute(select)
    for contato in cursor:
        print(contato['contato'], contato['grupo'])
except ProgrammingError as e:
    print('Erro: {e.msg}')
