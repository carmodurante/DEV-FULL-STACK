# Uso de argumentos nomeados


# Use apenas argumentos nomeados para garantir clareza de código
def minha_funcao(arg1, arg2, *, suprimir_exceptions=False):
    print(arg1, arg2, suprimir_exceptions)


def main():
    # Tente fazer a chamada da função sem o nome do argumento
    minha_funcao(1, 2, True)


if __name__ == "__main__":
    main()
