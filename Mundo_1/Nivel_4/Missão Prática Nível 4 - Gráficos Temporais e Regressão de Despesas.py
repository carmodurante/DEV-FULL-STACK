import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

class graficos:

    def __init__(self):
        url = "https://raw.githubusercontent.com/carmodurante/content/main/Despesas.csv"
        self.despesas = pd.read_csv(url, sep=';')

    def visualizar_graf_temporal(self):
        sns.set_style("darkgrid")
        # Tamanho do Gráfico
        plt.figure(figsize=(15, 5))
        # Linhas
        sns.lineplot(x='Dia', y='Alimentacao', data=self.despesas, label='Alimentação', marker='o', markersize=10)
        sns.lineplot(x='Dia', y='Vestuario', data=self.despesas, label='Vestuário', marker='o', markersize=10)
        sns.lineplot(x='Dia', y='Transporte', data=self.despesas, label='Transporte', marker='o', markersize=10)
        ax = sns.lineplot()
        # Estilos
        for lines in ax.lines:
            lines.set_linestyle("--")
            lines.set_linewidth(3)
        # Titulo dos Eixos
        plt.ylabel('Despesas em R$')
        plt.xlabel('Dia')
        # Posição dos Ticks
        plt.xticks(ticks=self.despesas['Dia'].tolist(), labels=self.despesas['Dia'].tolist())
        # Exibir Gráfico
        plt.show()

    def visualizar_regressao_linear(self):
        sns.set_style("darkgrid")
        # Tamanho do Gráfico
        plt.figure(figsize=(15, 5))
        # Calcula Regressão
        alimentacao = self.despesas[['Alimentacao']]
        dias = self.despesas[['Dia']]
        regr = LinearRegression()
        regr.fit(X=dias, y=alimentacao)
        # Linhas
        plt.plot(dias, regr.predict(dias), color='red', linewidth=4, label='Regressão Linear')
        sns.lineplot(x='Dia', y='Alimentacao', data=self.despesas, label='Alimentação - Original', marker='o',
                     markersize=12)
        # Estilos
        ax = sns.lineplot()
        for idx, lines in enumerate(ax.lines):
            if idx > 0:
                lines.set_linestyle("--")
                lines.set_linewidth(3)
        # Posição dos Ticks
        plt.xticks(ticks=self.despesas['Dia'].tolist(), labels=self.despesas['Dia'].tolist())
        # Titulo dos Eixos
        plt.xlabel('Dias')
        plt.ylabel('Despesas em R$')
        # Exibir Gráfico
        plt.show()


if __name__ == '__main__':
    graficos = graficos()
    graficos.visualizar_graf_temporal()
    graficos.visualizar_regressao_linear()
