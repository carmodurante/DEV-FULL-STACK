palavras = ('aprender', 'programar', 'linguagem', 'python', 'gratis', 'estudar')
vogais = ('a', 'e', 'i', 'o', 'u')


for elementos in palavras:
    lista_vogais = ''
    for letra in elementos:
        if letra in vogais:
            lista_vogais += letra

    print(f'Na palavra {elementos.upper()} temos: {" ".join(lista_vogais)}')