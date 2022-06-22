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