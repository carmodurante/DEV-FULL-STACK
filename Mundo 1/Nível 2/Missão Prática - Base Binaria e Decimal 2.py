# Missão Prática Nível 2 — Base Binária e Decimal
# Autor: Carmo Durante Neto

numero_base_decimal = eval(input('Digite um numero inteiro: '))
# Permite apenas numeros inteiros positivos
if type(numero_base_decimal) is int and numero_base_decimal >= 0:

    binario_string = ''
    decimal = numero_base_decimal

    while numero_base_decimal > 0:
        # Resto da divisão em ‘string’
        binario_string += str(numero_base_decimal % 2)
        # Divisão inteira
        numero_base_decimal //= 2

    print(f'Numero na base decimal:{decimal}')
    # Imprime os valores da ‘string’ de trás para frente.
    print(f'Numero na base binaria:{binario_string[::-1]}')
else:
    print("Não é um numero inteiro!")
