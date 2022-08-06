# Usando objetos defaultdict
import collections

def main():
    # Definindo uma lista de itens para contar
    frutas = ['maçã', 'pêra', 'laranja', 'banana',
              'maçã', 'uva', 'banana', 'banana']

    # TODO: Use um dicionário default para contar cada elemento
    contador_frutas = {}

    # Conte os elementos da lista
    for fruta in frutas:
        contador_frutas[fruta] += 1

    # Faça o print do resultado
    for (c, v) in contador_frutas.items():
        print(c + ": " + str(v))


if __name__ == "__main__":
    main()
    