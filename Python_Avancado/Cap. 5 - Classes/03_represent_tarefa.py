# Personalizando representações string de classes


class Pessoa():
    def __init__(self):
        self.nome = "Jessica"
        self.sobrenome = "Temporal"
        self.idade = 25

    # TODO: Use __repr__ para criar uma string que seja útil para debug

    # TODO: Use __str__ para criar uma string amigável para humanos

    # TODO: Use bytes para converter a string em um objeto bytes


def main():
    # Criando uma instância de Pessoa
    pessoa = Pessoa()

    # Usando as funções embutidas de Python para representar a pessoa
    # numa string
    print(repr(pessoa))
    print(str(pessoa))
    print("Formatado: {0}".format(pessoa))


if __name__ == "__main__":
    main()
