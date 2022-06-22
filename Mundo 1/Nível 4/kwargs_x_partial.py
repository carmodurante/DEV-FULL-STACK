from functools import partial


def compra(total, **kwargs):
    # Torna essas váriaveis "Parametros Opcionais
    desconto = kwargs.get('desconto')
    tax = kwargs.get('tax')

    # Verifica se as váriaveis foram criadas not (typeNone) ( is not initial )
    if desconto:
        total -= total * (desconto / 100)

    if tax:
        total += total * (tax / 100)

    return total


total_compra = compra(121)
print(total_compra)  # Saida --> 121

total_compra = compra(120, tax=5)
print(total_compra)  # Saida --> 126

total_compra = compra(100, tax=7, desconto=10)
print(total_compra)  # Saida --> 96.3


# Desabilitando Parametros de uma função.
# Def partial(compra, total, tax, desconto):
#     def compra_nova(total, tax=None, desconto=None):
#         return compra(total)
#     return compra_nova


def compra_v2(total, desconto, tax):

    # Verifica se as váriaveis foram criadas not (typeNone) ( is not initial )
    if desconto:
        total -= total * (desconto / 100)

    if tax:
        total += total * (tax / 100)

    return total


compra_nova = partial(compra_v2, desconto=None, tax=None)

print(compra_nova(100, desconto=100, tax=100))  # saida --> 100
print(compra_nova(100, desconto=100))  # saida --> 100
print(compra_nova(100, tax=100))  # saida --> 100
print(compra_nova(100))  # saida --> 100
print(compra_v2(100, None, None))  # Passar None é a "mesma coisa"
