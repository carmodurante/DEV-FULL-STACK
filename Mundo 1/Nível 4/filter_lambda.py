# script funcao_filter_lambda.py
lista = [1, 2, 3, 4, 5]

nova_lista = filter(lambda item: item % 2 != 0, lista)


def main():
    print(list(nova_lista))


if __name__ == "__main__":
    main()
