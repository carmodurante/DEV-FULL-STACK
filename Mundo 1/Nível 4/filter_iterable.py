# script funcao_filtro_iterable.py
lista = [1, 2, 3, 4, 5]


def impares(iterable):
    lista_aux = []
    for item in iterable:
        if item % 2 != 0:
            lista_aux.append(item)
    return lista_aux


def main():
    nova_lista = impares(lista)
    print(nova_lista)

