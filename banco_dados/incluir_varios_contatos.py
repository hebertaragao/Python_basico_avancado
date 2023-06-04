from mysql.connector.errors import ProgrammingError
from bd import nova_conexao

sql = 'INSERT INTO contatos(nome, tel) VALUES (%s, %s)'
args = (
        ('Ana', '99765-4321'),
        ('Bia', '98865-4324'),
        ('Luca', '98775-4323'),
        ('Lu', '98766-4322'),
        ('Gui', '98755-4311'),
        ('Beca', '97865-3321'),
        ('Pedro', '98675-2321'),
)

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Foram incluídos {cursor.rowcount} registros!')
