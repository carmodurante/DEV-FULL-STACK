# script funcao4.py

# captando os valores do campo Input

valores = input()

# separando os valores pelo espaço em branco e

# transformando-os em uma lista de inteiros

valores = [int(i) for i in valores.split()]


def altera_lista(lista):
    nova_lista = list(lista)

    nova_lista[2] = nova_lista[2] + 10

    return nova_lista


def main():
    print("Nova lista", altera_lista(valores))

    print("Nova lista", altera_lista(valores))


if __name__ == "__main__":
    main()