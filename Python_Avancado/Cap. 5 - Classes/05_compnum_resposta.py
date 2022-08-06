# Imitando o comportamento de números numa classe


class Coordenada():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Coordenada x:{0},y:{1}>".format(self.x, self.y)

    # Implemente adição
    def __add__(self, other):
        return Coordenada(self.x + other.x, self.y + other.y)

    # Implemente subtração
    def __sub__(self, other):
        return Coordenada(self.x - other.x, self.y - other.y)

    # Implemente adição in-place
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def main():
    # Declare some Coordenadas
    c1 = Coordenada(10, 20)
    c2 = Coordenada(30, 30)
    print(c1, c2)

    # Adicionar duas Coordenadas
    c3 = c1 + c2
    print(c3)

    # Subtrair duas Coordenadas
    c4 = c2 - c1
    print(c4)

    # Executar uma adição in-place
    c1 += c2
    print(c1)


if __name__ == "__main__":
    main()
