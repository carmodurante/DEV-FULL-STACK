import xlrd

from Mundo_1.Nivel_5.Programa_Planilha.modelos import Variavel

planilha = xlrd.open_workbook_xls("Dicionarios_input/dicionario_pessoas.xls")
primeira_aba = planilha.sheet_by_index(0)  # Pode ser por nome
print("Nome:", primeira_aba.name)
print("Num linhas:", primeira_aba.nrows)
print("Num colunas:", primeira_aba.ncols)

variaveis = []
nova_variavel = None
for idx, linha in enumerate(primeira_aba.get_rows()):  # retona todas as linhas, e itera nas linhas.
    print(linha)
    primeira_celula = linha[0]
    if primeira_celula.ctype == 2: # number
        # Nova variavel
        if nova_variavel:
            # Guarda a ultima variavel
            variaveis.append(nova_variavel)
        # Variaveis de construtor
        posicao_inicial = linha[0].value
        tamanho = linha[1].value
        codigo = linha[2].value
        descricao = linha[4].value
        nova_variavel = Variavel(posicao_inicial, tamanho, codigo, descricao)
        # Variaveis da primeira categoria
        categoria_tipo = linha[5].value
        categoria_descricao_tipo = linha[6].value
        nova_variavel.add_categoria({'categoria_tipo': categoria_tipo,
                                     'categoria_descricao_tipo': categoria_descricao_tipo})
    else:
        if nova_variavel:
            # Variaveis das demais categorias
            categoria_tipo = linha[5].value
            categoria_descricao_tipo = linha[6].value
            nova_variavel.add_categoria({'categoria_tipo': categoria_tipo,
                                         'categoria_descricao_tipo': categoria_descricao_tipo})

    if idx > 50:
        break

print('Total de variaveis', len(variaveis))
for variavel in variaveis:
    print(variavel)
    for categ in variavel.categoria:
        print('\t', categ)
