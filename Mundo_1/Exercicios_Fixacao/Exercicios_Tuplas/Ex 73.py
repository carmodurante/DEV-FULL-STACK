classificacao = ('Palmeiras', 'Corinthians', 'São Paulo', 'Internacional', 'Athletico-PR', 'Atlético-MG',
                 'Coritiba', 'Fluminense', 'América-MG', 'Santos', 'Bragantino', 'Ceará', 'Goiás', 'Atlético-GO',
                 'Flamengo', 'Botafogo', 'Cuiabá', 'Avaí', 'Juventude', 'Fortaleza')

primeiros = []
ultimos = []
ordenados = []

# 5 primeiros
for time in classificacao[0:5]:
    primeiros.append(time)

# 5 ultimos
for time in classificacao[:-6:-1]:
    ultimos.append(time)

# Ordem alfabetica
for time in sorted(classificacao):
    ordenados.append(time)

# Posição do São Paulo
posicao = classificacao.index('Santos') + 1

print('Primeiros:')
print(primeiros)
print(classificacao[0:5])
print('************************')
print('Ultimos:')
print(ultimos)
print(classificacao[:-6:-1])
print('************************')
print('Ordem Alfabetica')
print(ordenados)
print(sorted(classificacao))
print('************************')
print('Posição Santos:')
print(f'Santos é o {posicao}ª colocado na tabela')
