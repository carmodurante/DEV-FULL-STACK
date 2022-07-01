# script funcao_iterable.py
lista = [1, 2, 3, 4, 5]


def triplica_itens(iterable):
    lista_aux = []
    for item in iterable:
        lista_aux.append(item * 3)
    return lista_aux


def main():
    nova_lista = triplica_itens(lista)
    print(nova_lista)


if __name__ == "__main__":
    main()
