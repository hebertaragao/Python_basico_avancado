#!Python3
compras = (
    {'quantidade': 2, 'preço': 10},
    {'quantidade': 3, 'preço': 20},
    {'quantidade': 5, 'preço': 14},
)

totais = tuple(
    map(
        lambda compra: compra['quantidade'] * compra['preço'],
        compras
    )
)

print('Preços totais: ', list(totais))
print('Total geral:', sum(totais))
