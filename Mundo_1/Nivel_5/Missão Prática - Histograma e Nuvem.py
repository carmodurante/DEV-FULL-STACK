import matplotlib.pyplot as plt
from faker import Faker


def cria_arquivo():
    with open("teste2.txt", "w") as arquivo:
        linhas = []
        faker = Faker()
        for i in range(100):
            linhas.append(f'{faker.name()};{faker.random_int(1, 10)}\n')
        arquivo.writelines(linhas)


def carrega_dados_arquivo():
    with open("teste2.txt", "r" ) as arquivo:
        arquivo_lista = arquivo.readlines()
        linhas_dicionario = {}
        for linhas in arquivo_lista:
            linhas_termos = linhas.split(";")
            linhas_dicionario['nome'] = linhas_termos[0]
            linhas_dicionario['pontuacao'] = linhas_termos.strip()

carrega_dados_arquivo()
# cria_arquivo()
# def dados_notas(nota_maxima, num_notas):
#     dados = []
#     faker = Faker()
#
#     for i in range(num_notas):
#         dados.append(faker.random_int(1, nota_maxima))
#
#     return dados
#
#
# if __name__ == '__main__':
#     plt.title('Histograma Pontuações', fontsize=20)
#     plt.xlabel('Pontuações', fontsize=15)
#     plt.ylabel('Probabilidade', fontsize=15)
#     plt.tick_params(labelsize=10)
#     plt.hist(dados_notas(10, 1000), density=True, rwidth=0.88, color='blue', alpha=0.7, edgecolor='black')
#     plt.show()
