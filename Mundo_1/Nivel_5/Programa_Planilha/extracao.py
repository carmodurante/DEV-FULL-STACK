import principal
import pandas

variaveis = principal.extrair_variaveis("Dicionarios_input/dicionario_pessoas.xls")

colunas = [str(variavel) for variavel in variaveis]
linhas = []
with open("Dados/pessoas_2015.txt") as microdados:
    for idx, linha in enumerate(microdados):
        nova_linha = []
        for variavel in variaveis:
            valor = linha[variavel.posicao_inicial:variavel.posicao_inicial + variavel.tamanho].strip()
            if valor:
                valor = int(valor)
            valor_final = variavel.categoria.get(valor) if variavel.categoria.get(valor) else valor
            nova_linha.append(valor_final)
        linhas.append(nova_linha)

df = pandas.DataFrame(linhas, columns=colunas)
# print(df.shape)
df.to_csv('microdados.csv', sep=';')
