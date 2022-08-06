# Usando lambdas como funções de uma linha


def celsius_para_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_para_celsius(temp):
    return (temp-32) * 5/9


def main():
    temp_em_c = [0, 12, 34, 100]
    temp_em_f = [32, 65, 100, 212]

    # TODO: Defina funções tradicionais para converter as temperaturas

    # TODO: Use lambdas tpara converter as temperaturas


if __name__ == "__main__":
    main()
