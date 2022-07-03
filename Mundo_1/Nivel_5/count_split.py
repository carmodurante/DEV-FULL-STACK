# Count
with open("teste2.txt") as arquivo:
    texto =  arquivo.read()
    contador = texto.count("linha")
    print("Total de Olas: ", contador)

# Split
frase1 = "Eu amo amoras no café da manhã"
lista_termos1 = frase1.split()
print(lista_termos1)

frase2 = "Amora abacaxi abacate       banana"
lista_termos2 = frase2.split()
print(lista_termos2)

frase3 = "carro,moto,banana"
lista_termos3 = frase3.split(',')
print(lista_termos3)
