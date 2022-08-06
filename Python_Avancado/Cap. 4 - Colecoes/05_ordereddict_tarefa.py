# Usando objetos OrderedDict
from collections import OrderedDict


def main():
    # Lista de times com número de partidas perdidadas e ganhas
    times_fut = [("Cruzeiro", (18, 12)), ("Vasco", (24, 6)), 
                 ("Avaí", (20, 10)), ("Flamengo", (22, 8)),
                 ("Palmeiras", (15, 15)), ("Santos", (20, 10)), 
                 ("Botafogo", (16, 14)), ("Fluminense", (25, 5))]

    # Ordenando os times pela quantidade de vitórias
    times_ord = sorted(times_fut, key=lambda t: t[1][0], reverse=True)

    # TODO: Crie um dicionário ordenado com os times

    # TODO: Use popitem para remover o item do topo

    # TODO: Faça um teste de igualdade


if __name__ == "__main__":
    main()
