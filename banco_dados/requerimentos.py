#!python
try:
    from mysql import conncetor
except ModuleNotFoundError:
    print('MySQL Connector não instalado!')
else:
    print('MySQL Connector instalado e pronto!')
