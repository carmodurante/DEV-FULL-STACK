import matplotlib.pyplot as plt
from faker import Faker
from wordcloud import WordCloud


def cria_arquivo():
    with open("dados_pontuacao.txt", "w") as arquivo:
        linhas = []
        faker = Faker()
        for i in range(100):
            linhas.append(f'{faker.name()};{faker.random_int(1, 10)}\n')
        arquivo.writelines(linhas)


def carrega_dados_arquivo():
    with open("dados_pontuacao.txt", "r") as arquivo:
        arquivo_lista = arquivo.readlines()
        lista_pontuacao = []
        linhas_dicionario = {"Nome": [], "Pontuacao": []}
        for linhas in arquivo_lista:
            linhas = linhas.strip()
            linhas_termos = linhas.split(";")
            linhas_dicionario['Nome'].append(linhas_termos[0])
            linhas_dicionario['Pontuacao'].append(int(linhas_termos[1]))
            lista_pontuacao.append(int(linhas_termos[1]))
    return linhas_dicionario, lista_pontuacao


def exibir_histograma(lista_pontuacao):
    plt.title('Histograma Pontuações', fontsize=20)
    plt.xlabel('Pontuações', fontsize=15)
    plt.ylabel('Probabilidade', fontsize=15)
    plt.tick_params(labelsize=10)
    plt.hist(lista_pontuacao, density=True, rwidth=0.88, color='blue', alpha=0.7, edgecolor='black')
    plt.show()


def exibir_nuvem_palavras():
    a = 1


if __name__ == '__main__':
    cria_arquivo()  # Cria arquivo
    lista_arquivo, lista_pontuacao = carrega_dados_arquivo()  # Carrega dados do arquivo
    exibir_histograma(lista_pontuacao)
