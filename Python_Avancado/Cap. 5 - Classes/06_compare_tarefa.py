# Usando métodos mágicos para comparar objetos entre si


class Pessoa():
    def __init__(self, nome, sobrenome, nivel, anos_trabalhados):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nivel = nivel
        self.senioridade = anos_trabalhados

    # TODO: Implemente as comparações usando o nível de cada pessoa
    def __ge__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass



def main():
    # Definindo pessoas
    dpto = []
    dpto.append(Pessoa("Túlio", "Toledo", 5, 9))
    dpto.append(Pessoa("João", "Junior", 4, 12))
    dpto.append(Pessoa("Jessica", "Temporal", 6, 6))
    dpto.append(Pessoa("Rebeca", "Robinson", 5, 13))
    dpto.append(Pessoa("Thiago", "Tavares", 5, 12))

    # TODO: Descobrindo quem é mais sênior

    # TODO: Organizando as pessoas por senioridade


if __name__ == "__main__":
    main()
