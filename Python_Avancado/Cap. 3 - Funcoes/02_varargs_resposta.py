# Uso de argumentos variáveis


# Defina uma função que recebe argumentos variáveis
def adicao(*args):
    return sum(args)


# Função com um argumento posicional
# def adicao(base, *args):
#     return sum(args)


def main():
    # Passe argumentos diferentes para o método adicao()
    print(adicao(5, 10, 15, 20))
    print(adicao(1, 2, 3))

    # Passe uma lista para o método adicao()
    numeros = [5, 10, 15, 20]
    print(adicao(*numeros))


if __name__ == "__main__":
    main()
