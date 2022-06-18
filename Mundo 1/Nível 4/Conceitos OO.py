class Conta:
    # Atributos privados __
    def __init__(self, numero, saldo):
        self.__numero = numero
        self.__saldo = saldo
        print(self.__saldo)


def main():
    conta = Conta(1, 1000)
    saldo = conta.__saldo


if __name__ == "__main__":
    main()
