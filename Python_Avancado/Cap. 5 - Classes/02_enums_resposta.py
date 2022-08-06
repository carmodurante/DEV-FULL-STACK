# Definindo enumarações usando a classe Enum de base

from enum import Enum, auto


# TODO: Defina a classe Fruta que herda de Enum
class Fruta(Enum):
    UVA = 1
    BANANA = 2
    LARANJA = 3
    TOMATE = 4
    PERA = auto()


def main():
    # Objetos enum possuem valores e tipos de fácil leitura
    print(Fruta.UVA)
    print(type(Fruta.UVA))
    print(repr(Fruta.UVA))

    # Objetos enum possuem propriedades "name" (nome) e "value" (valor)
    print(Fruta.UVA.name, Fruta.UVA.value)

    # Mostre o valor gerado automaticamente para PERA
    print(Fruta.PERA.value)

    # É possível usar objetos enum como chaves
    minhas_frutas = {}
    minhas_frutas[Fruta.BANANA] = "Fruta amarela"
    print(minhas_frutas[Fruta.BANANA])


if __name__ == "__main__":
    main()
