arquivo = open("teste.txt")

arquivo_iteravel = open("teste.txt", "r")

index = 0

for linha in arquivo_iteravel:
    index += 1
    print(f'linha {index} - {linha}')

# conteudo = arquivo.read()
conteudo_lista = arquivo.readlines()

print('nome do arquivo: ', arquivo.name)
print('modo do arquivo: ', arquivo.mode)
print('nome do arquivo: ', arquivo.closed)
# print('Conteudo: ', repr(conteudo))
print('Conteudo Lista: ', repr(conteudo_lista))

arquivo.close()

print('nome do arquivo: ', arquivo.closed)