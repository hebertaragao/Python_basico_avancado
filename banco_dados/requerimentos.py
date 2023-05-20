#!/usr/bin/python3
try:
    from mysql import connector
except ModuleNotFoundError:
    print('MySQL connector não instalado!')
else:
    print('MySQL Connector instalado e pronto!')