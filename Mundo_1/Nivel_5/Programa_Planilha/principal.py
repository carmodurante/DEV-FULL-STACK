import xlrd

from Mundo_1.Nivel_5.Programa_Planilha.modelos import Variavel


def extrair_variaveis(dicionario):
    planilha = xlrd.open_workbook_xls(dicionario, encoding_override='latin1')
    primeira_aba = planilha.sheet_by_index(0)  # Pode ser por nome

    variaveis = []
    nova_variavel = None
    for idx, linha in enumerate(primeira_aba.get_rows()):  # retona todas as linhas, e itera nas linhas.
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
            categoria_tipo = int(linha[5].value) if linha[5].ctype == 2 else linha[5].value
            categoria_descricao_tipo = int(linha[6].value) if linha[6].ctype == 2 else linha[6].value
            nova_variavel.add_categoria({'categoria_tipo': categoria_tipo,
                                         'categoria_descricao_tipo': categoria_descricao_tipo})
        else:
            if nova_variavel:
                # Variaveis das demais categorias
                if primeira_celula.ctype == 0:
                    categoria_tipo = int(linha[5].value) if linha[5].ctype == 2 else linha[5].value
                    categoria_descricao_tipo = int(linha[6].value) if linha[6].ctype == 2 else linha[6].value
                    nova_variavel.add_categoria({'categoria_tipo': categoria_tipo,
                                             'categoria_descricao_tipo': categoria_descricao_tipo})

    return variaveis
