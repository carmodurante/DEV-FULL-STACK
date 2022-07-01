def soma(lista):
    if sum(lista) == 35:
        print('sucesso')
    else:
        print('erro')

    assert sum(lista) == 35, 'Sucesso'


lista = [5, 10, 20]
soma(lista)