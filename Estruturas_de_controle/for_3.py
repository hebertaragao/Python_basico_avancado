produto = {'Nome': 'Caneta chic', 'Preço': 14.99,
           'Importada': True, 'Estoque': 793}

for chave in produto:
    print(chave)

for valor in produto.values():
    print(valor)

for chave, valor in produto.items():
    print(chave, '=', valor)
