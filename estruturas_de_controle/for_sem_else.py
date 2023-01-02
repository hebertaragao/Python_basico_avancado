# Palavras escritas em caixa alta são dadas como constantes no python
PALAVRAS_PROIBIDAS = ('Futebol', 'Religião', 'Política')
textos = [
    'João gosta de futebol e Política',
    'A praia foi divertida',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado: ', texto)
