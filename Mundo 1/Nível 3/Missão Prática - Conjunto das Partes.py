# Missão Prática Nível 3 — Conjunto das Partes.
# Autor: Carmo Durante Neto

# Calcula todos os conjuntos possiveis
def conjuntos_possiveis(lista_elementos):
    if not lista_elementos:
        return [[]]
    else:
        # Verifica recursivamente as combinações da posição n com a posição n+1
        # Concatena o "final" retorno dos subelementos do retorno da chamada n+sub_elemento da função
        elemento = conjuntos_possiveis(lista_elementos[1:])
        return elemento + [[lista_elementos[0]] + sub_elemento for sub_elemento in elemento]


# Retorna uma lista de conjuntos do tamanho indicado
def subconjuntos_por_tamanho(lista_conjuntos, numero):
    lista_subconjuntos = []
    for elementos in lista_conjuntos:
        if len(elementos) == numero:
            lista_subconjuntos.append(elementos)
    return lista_subconjuntos


def exibe_conjuntos(lista_elementos, tamanho_conjunto):
    print(f'Conjunto de {tamanho_conjunto} elemento(s): {lista_elementos}')

    # Imprime todos os conjuntos do menor para o maior.
    for numero in range(tamanho_conjunto+1):
        lista_subconjuntos = sorted(subconjuntos_por_tamanho(conjuntos_possiveis(lista_elementos), numero))
        print(f'Conjunto de {numero} elemento(s): {lista_subconjuntos}')


# Dados de entrada do usuário
def dados_entrada():
    # Declarações
    tamanho_conjunto = 0
    lista_elementos = []
    resposta = 's'

    while resposta not in 'nN':
        tamanho_conjunto += 1
        lista_elementos.append(input(f'Digite o {tamanho_conjunto}º elemento do conjunto: '))
        resposta = input('Deseja continuar adicionando elementos? S/N: ')
    return lista_elementos, tamanho_conjunto


if __name__ == '__main__':
    lista_elementos, tamanho_conjunto = dados_entrada()
    exibe_conjuntos(lista_elementos, tamanho_conjunto)
