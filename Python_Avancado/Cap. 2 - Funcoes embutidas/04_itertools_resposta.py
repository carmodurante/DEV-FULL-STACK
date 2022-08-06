# Iteradores do módulo itertools
import itertools


def condicao(x):
    return x < 40


def main():
    # Iterador cycle pode ser usado como o iter para iterar sobre
    # uma lista
    pessoas = ["Jessica", "Leticia", "Gustavo"]
    ciclo = itertools.cycle(pessoas)
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))

    # use count to create a simple counter
    contador = itertools.count(100, 10)
    print(next(contador))
    print(next(contador))
    print(next(contador))

    # A função accumulate cria um iterdor que acumula valores
    valores = [10, 20, 30, 40, 50, 40, 30]
    acumulado = itertools.accumulate(valores, max)
    print(list(acumulado))

    # Use a função chain para conectar listas
    x = itertools.chain("ABCD", "1234")
    print(list(x))

    # As funções dropwhile e takewhile vai retornar valores até
    # que uma condição seja atingida
    print(list(itertools.dropwhile(condicao, valores)))
    print(list(itertools.takewhile(condicao, valores)))


if __name__ == "__main__":
    main()
