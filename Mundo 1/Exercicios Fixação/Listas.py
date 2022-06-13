# Append and Inserts
lista = list()
lista.append('carro')
print(lista)

lista.append('moto')
print(lista)

lista.insert(1, 'bicicleta')  ##← Inserimos o elemento bicicleta na posição de índice 1
print(lista)

# Media
lista = [1, 3, 5, 7, 9]
media = sum(lista) / len(lista)
print(media)
print(max(lista))
print(min(lista))

# Operadores
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [4, 5, 6]
print(lista1 == lista2)

print(lista1 == lista3)

if 3 in lista1:
    print('Achei o 3!!!')

nova_lista = lista1 + lista3
print(nova_lista)

lista_repetida = lista1 * 4
print(lista_repetida)

# Compreensão de listas (do inglês list comprehensions).
# [item for item in lista]
lista = [1, 2, 3]
nova_lista = [item * 2 for item in lista]
print(nova_lista)
# [item for item in lista if item cond]
# Por exemplo: item > 0, item == 'a', item.startswith('b') etc.
lista = [0, 1, 2, 3, 4, 5, 6]
nova_lista = [item for item in lista if item % 2 == 0]
print(nova_lista)
