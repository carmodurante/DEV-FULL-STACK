arquivo = open("teste.txt")

print('nome do arquivo: ', arquivo.name)
print('modo do arquivo: ', arquivo.mode)
print('nome do arquivo: ', arquivo.closed)

arquivo.close()

print('nome do arquivo: ', arquivo.closed)