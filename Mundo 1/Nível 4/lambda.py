# script funcao_map_lambda.py
lista = [1, 2, 3, 4, 5]

# O primeiro parametro de map é (lambda item: item * 3) Função (lambda) com parametro 'item' e o parametro
# 'item' é multiplicado por 3, a nivel de elemento.

# Para cada ‘item’ de lista irá entrar na função lambda no parametro ‘item’ e será multiplicado por 3.

nova_lista = map(lambda item: item * 3, lista)  # função (lambda)


def main():
    print(list(nova_lista))


if __name__ == "__main__":
    main()
