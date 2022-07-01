arquivo_escreve = open("teste2.txt", "w")  # Escreve com Truncate.

arquivo_escreve.write("Parelelepipedo")

linhas = ["\nlinha 1. \n", "linha 2."]

arquivo_escreve.writelines(linhas)

arquivo_escreve.close()

#################################################

arquivo_adiciona = open("teste2.txt", "a")  # Escreve appendando

linhas = ["\nlinha 3. \n", "linha 4."]

arquivo_adiciona.writelines(linhas)

arquivo_escreve.close()
