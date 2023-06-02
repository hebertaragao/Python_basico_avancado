from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='K@rdec1857'
)

cursor = conexao.cursor()
cursor.execute('SHOW DATABASE')

for i, database in enumerate(cursor):
    print(f'Banco de dados {i}:{database[0]}')
