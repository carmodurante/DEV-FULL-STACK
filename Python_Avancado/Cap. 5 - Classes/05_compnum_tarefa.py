# Imitando o comportamento de números numa classe


class Coordenada():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Coordenada x:{0},y:{1}>".format(self.x, self.y)

    # TODO: Implemente adição
    def __add__(self, other):
        pass

    # TODO: Implemente subtração
    def __sub__(self, other):
        pass

    # TODO: Implemente adição in-place
    def __iadd__(self, other):
        pass


def main():
    # Declare some Coordenadas
    c1 = Coordenada(10, 20)
    c2 = Coordenada(30, 30)
    print(c1, c2)

    # TODO: Adicionar duas Coordenadas

    # TODO: Subtrair duas Coordenadas

    # TODO: Executar uma adição in-place


if __name__ == "__main__":
    main()
