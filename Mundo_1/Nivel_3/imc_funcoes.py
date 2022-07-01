def calcula_imc(peso, altura):
    imc = float(peso) / float(altura) ** 2
    return imc


def classifica_imc(indice):
    if indice < 18.5:
        return 'Abaixo do peso ideal'
    elif indice < 25:
        return 'Peso ideal'
    elif indice < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade, vai se cuidar!'
