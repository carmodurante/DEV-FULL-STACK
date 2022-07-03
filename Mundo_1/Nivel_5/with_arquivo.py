print('Iterando Arquivo')

with open("teste2.txt") as arquivo:  # Não é necessário se preocupar com fechar o arquivo
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(linha_limpa)
    print("Fim do arquivo", arquivo.name)
