from multiprocessing import Process

minha_lista = []


def funcao_a(indice):
    for i in range(10):
        minha_lista.append(1)
        print("Termino thread ", indice)


def main():
    tarefas = []
    for indice in range(10):
        tarefa = Process(target=funcao_a, args=(indice,))
        tarefas.append(tarefa)
        tarefa.start()

    print("Antes de aguardar o termino!", len(minha_lista))

    for tarefa in tarefas:
        tarefa.join()

    print(f'Após aguardar o termino! {len(minha_lista)} Tarefa: {tarefa}')


if __name__ == "__main__":
    main()
