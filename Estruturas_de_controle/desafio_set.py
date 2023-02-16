PALAVRAS_PROIBIDAS = {'Futebol', 'Religião', 'Política'}
textos = [
    'João gosta de futebol e Política',
    'A praia foi divertida',
]

for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto possui palavras proibidas: ', intersecao)
    else:
        print('Texto autorizado:', texto)
