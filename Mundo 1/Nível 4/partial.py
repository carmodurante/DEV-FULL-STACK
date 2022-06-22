from functools import partial


def soma(x, y):
    return x + y


# Salva a função soma com o primeiro parametro preenchido (no caso é x), a função será salva na nova_soma
nova_soma = partial(soma, 1)  # Atribuindo um valor padrão para x.

# Agora x esta "desativado" na função nova_soma() e não pode ser setado.
# Porque já foi preenchido anteriormento com o valor 1 (internamente ele fica em uma tupla)
print(nova_soma(4))  # saída --> 4

nova_soma_v2 = partial(soma, y=3)  # Atribuindo um valor padrão para y.
print(nova_soma_v2(5))  # saída --> 8
print(nova_soma_v2(5, y=10))  # saída --> 15
