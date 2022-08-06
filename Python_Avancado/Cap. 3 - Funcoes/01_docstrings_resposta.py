# Usando docstrings para documentar métodos


def minha_funcao(arg1, arg2=None):
    """Minha função que faz um print

    Params:
        arg1: primeiro argumento. O que você quiser passar.
        arg2: segundo argumento. Default: None. O que te fizer feliz.
    """
    print(arg1, arg2)


def main():
    print(minha_funcao.__doc__)


if __name__ == "__main__":
    main()
