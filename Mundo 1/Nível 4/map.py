# script funcao_map.py
lista = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]


def triplica(item, item2):
    return item * item2


def main():
    # O primeiro parametro de map é a função pré definida com a quantidade de parametros certas.
    # Os outros parametros serão listas/tuplas etc, e ira percorrer ‘item’ por ‘item’
    # é possivel falar a ordem que vai os itens com [::-1]
    nova_lista = map(triplica, lista, lista2[::-1])
    print(list(nova_lista))


if __name__ == "__main__":
    main()
