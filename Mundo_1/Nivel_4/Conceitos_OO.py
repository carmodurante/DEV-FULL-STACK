import math


class Math:
    @staticmethod
    def sqrt(x):
        return math.sqrt(x)


class Conta:
    # Atributos privados __
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        print(self.__saldo)


def main():
    conta = Conta(1, 1000)
    saldo = conta.__saldo
    # O interpretador renomeia o atributo privado para _nomedaClasse__nomedoatributo.
    saldo = conta._Conta__saldo


if __name__ == "__main__":
    main()
