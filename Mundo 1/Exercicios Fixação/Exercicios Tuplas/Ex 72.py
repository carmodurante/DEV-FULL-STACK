numerosExtenso = ('Um', 'Dois', 'Tres', 'Quatro', 'Cinco')

numero = 6

while not 0 < numero <= 5:
    numero = int(input('Digite um numero de 1 a 5: '))

    if 0 < numero <= 5:
        print(f'{numerosExtenso[numero - 1]}')
    else:
        print('Tente Novamente')
