# cada import deve ter a sua própria linha
import sys
import os


# duas linhas em branco separam classes de outras funções
class MinhaClasse():
    def __init__(self):
        self.descricao = "Minha Classe"

    # dentro de uma classe, usamos uma linha em branco entre métodos
    def meu_metodo(self, arg1):
        pass


def main():
    # comentários que usam mais de uma linha, devem ser limitados a 72
    # caracteres por linha
    instancia = MinhaClasse()
    print(instancia.descricao)
    instancia.descricao = "Classe da Jess"
    print(instancia.descricao)


if __name__ == "__main__":
    main()
