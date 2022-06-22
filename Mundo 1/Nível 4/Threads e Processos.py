from threading import Thread
from multiprocessing import Process


def funcao_a(nome):
    print(nome)


# Processos e Threads tem os contrutores e metodos muito parecidos.
def main():
    # Função que deverá ser executada (target) e quais parâmetros serão passados para essa função (args).
    # O parâmetro args espera um iterável (lista, tupla etc.), onde cada elemento será mapeado para um parâmetro
    # da função target.

    t = Thread(target=funcao_a, args=("Minha Thread",))
    t.start()  # Inicia a Thread com os parametros passados.

    p = Process(target=funcao_a, args=("Meu Processo",))
    p.start()  # Inicia o Processo com os parametros passados.


if __name__ == '__main__':
    main()
