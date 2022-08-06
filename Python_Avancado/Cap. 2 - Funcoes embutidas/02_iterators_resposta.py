# Usando funções iteradoras como enumerate, zip, iter, next


def main():
    # Defina a lista de dias da semana em Português e English
    dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
    dias_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # Use a função iter para criar um iterador sobre uma lista
    iterador_dias = iter(dias)
    print(next(iterador_dias))  # Dom
    print(next(iterador_dias))  # Seg
    print(next(iterador_dias))  # Ter

    # Use uma função para iterar sobre um arquivo
    with open("dados.txt", "r") as fp:
        for linha in iter(fp.readline, ''):
            print(linha)

    # Use a iteração tradicional (range) sobre a lista dias
    for m in range(len(dias)):
        print(m+1, dias[m])

    # Usar a função enumerate reduz a quantidade de código e te
    # dá um contador
    for i, m in enumerate(dias, start=1):
        print(i, m)

    # Use a função zip para combinar as listas
    for m in zip(dias, dias_en):
        print(m)

    # Combine zip com enumerate para formatar o resultado
    for i, m in enumerate(zip(dias, dias_en), start=1):
        print(i, m[0], "=", m[1], "em Inglês")


if __name__ == "__main__":
    main()
