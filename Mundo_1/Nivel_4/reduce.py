from functools import reduce

list_numbers = [1, 3, 4, 5, 6, 7, 8, 9]  # lista


# seu método soma.
def soma(x, y):
    return x + y


# Usando o método soma
result = soma(1, 3)
print(result)

# agora, com a função reduce
# Chama a função e uma lista
# Pega a lista e passa como parametros em ordem que esta na lista
# primeira execução 1 e 3 retorna 4, pega 4 (resultado) e o proximo numero da lista que tbm é 4.
reduce_soma = reduce(soma, list_numbers)
print(reduce_soma)  # saida --> 43
