# Usando métodos mágicos para comparar objetos entre si


class Pessoa():
    def __init__(self, nome, sobrenome, nivel, anos_trabalhados):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nivel = nivel
        self.senioridade = anos_trabalhados

    # Implemente as comparações usando o nível de cada pessoa
    def __ge__(self, other):
        if self.nivel == other.nivel:
            return self.senioridade >= other.senioridade
        return self.nivel >= other.nivel

    def __gt__(self, other):
        if self.nivel == other.nivel:
            return self.senioridade > other.senioridade
        return self.nivel > other.nivel

    def __lt__(self, other):
        if self.nivel == other.nivel:
            return self.senioridade < other.senioridade
        return self.nivel < other.nivel

    def __le__(self, other):
        if self.nivel == other.nivel:
            return self.senioridade <= other.senioridade
        return self.nivel <= other.nivel


def main():
    # Definindo pessoas
    dpto = []
    dpto.append(Pessoa("Túlio", "Toledo", 5, 9))
    dpto.append(Pessoa("João", "Junior", 4, 12))
    dpto.append(Pessoa("Jessica", "Temporal", 6, 6))
    dpto.append(Pessoa("Rebeca", "Robinson", 5, 13))
    dpto.append(Pessoa("Thiago", "Tavares", 5, 12))

    # Descobrindo quem é mais sênior
    print(bool(dpto[0] > dpto[2]))
    print(bool(dpto[4] < dpto[3]))

    # Organizando as pessoas por senioridade
    pessoas = sorted(dpto)
    for pessoa in pessoas:
        print(pessoa.p_nome)


if __name__ == "__main__":
    main()
