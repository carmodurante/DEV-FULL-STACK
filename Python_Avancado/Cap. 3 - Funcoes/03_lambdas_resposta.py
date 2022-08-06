# Usando lambdas como funções de uma linha


def celsius_para_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_para_celsius(temp):
    return (temp-32) * 5/9


def main():
    temp_em_c = [0, 12, 34, 100]
    temp_em_f = [32, 65, 100, 212]

    # Use regular functions to convert temps
    print(list(map(fahrenheit_para_celsius, temp_em_f)))
    print(list(map(celsius_para_fahrenheit, temp_em_c)))

    # Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t-32) * 5/9, temp_em_f)))
    print(list(map(lambda t: (t * 9/5) + 32, temp_em_c)))


if __name__ == "__main__":
    main()
