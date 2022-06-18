class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("saldo inválido")
        else:
            self._saldo = saldo


def main():
    conta = Conta(1)
    conta.saldo = 1000  # usando o @saldo.setter
    print(f'saldo da conta = {conta.saldo}')  # usando o @property


if __name__ == "__main__":
    main()
