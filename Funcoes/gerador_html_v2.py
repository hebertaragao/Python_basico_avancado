#!python
def tag_bloco(texto, classe='Sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('inline e classse', 'info', True))
    print(tag_bloco('inline', inline=True))
    print(tag_bloco('falhou', classe='error'))
