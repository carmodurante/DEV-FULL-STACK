from random import randint

numeros = []
for elemento in range(5):
    numeros.append(randint(0, 9))

numeros_tuple = tuple(numeros)

print(f'Numeros aleatorios na tupla: {numeros_tuple}')
print(f'Menor numero: {min(numeros_tuple)}')
print(f'Maior numero: {max(numeros_tuple)}')
