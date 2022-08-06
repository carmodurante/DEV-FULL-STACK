# Usando list comprehensions


def main():
    # Definindo duas listas de números ímpares e pares
    pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # Use map() e list() para calcular numeros ao quadrado
    pares_quadrado = list(map(lambda n: n**2, pares))
    print(pares_quadrado)

    # TODO: Crie uma lista nova a partir de uma lista preexistente

    # TODO: Use o predicado para limitar os itens


if __name__ == "__main__":
    main()
