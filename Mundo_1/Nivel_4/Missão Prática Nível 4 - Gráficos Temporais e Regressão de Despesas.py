import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class carrega_dados():

    def carrega_arquivo(self):
        arquivo_despesas = pd.read_csv("Despesas.csv", sep=';')

        print(arquivo_despesas)

        return arquivo_despesas

    def visualizar_graf_temporal(self, despesas):
        plt.figure(figsize=(5,15))
        ax = sns.lineplot(x='Dia', y='Alimentacao', data=despesas, label='Alimentação', marker='o')
        ax.lines[0].set_linestyle("--")
        plt.ylabel('Despesas em Reais')
        plt.xlabel('Dia')
        plt.xticks(ticks=despesas['Dia'].tolist(), labels=despesas['Dia'].tolist())
        plt.show()

if __name__ == '__main__':
    classe_dados = carrega_dados()
    despesas = classe_dados.carrega_arquivo()
    classe_dados.visualizar_graf_temporal(despesas)