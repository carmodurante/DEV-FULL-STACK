# Missão Prática Nível 3 — Conjunto das Partes.
# Autor: Carmo Durante Neto

class Cores:
    header = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    endColor = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


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


# Imprime na tela os conjuntos separados por tamanho de partes
def exibe_conjuntos(lista_elementos):
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f'{Cores.bold}{Cores.header}Conjunto de {Cores.cyan}{len(lista_elementos)}{Cores.endColor}'
          f'{Cores.bold}{Cores.header} elemento(s) digitados: {Cores.endColor}{Cores.endColor}'
          f' {Cores.cyan}{lista_elementos}{Cores.endColor}')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(
        f'{Cores.header}Total de conjuntos possíveis:{Cores.endColor} {Cores.cyan}{2 ** len(lista_elementos)}{Cores.endColor}')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    # Imprime todos os conjuntos do menor para o maior.
    for numero in range(len(lista_elementos) + 1):
        lista_subconjuntos = sorted(subconjuntos_por_tamanho(conjuntos_possiveis(lista_elementos), numero))
        print(f'{Cores.red}{len(lista_subconjuntos)}{Cores.endColor} Conjunto de {Cores.cyan}{numero}{Cores.endColor}'
              f' elemento(s): {Cores.cyan}{lista_subconjuntos}{Cores.endColor}')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


# Dados de entrada do usuário
def dados_entrada():
    # Declarações
    tamanho_conjunto = 0
    lista_elementos = []
    resposta = 's'
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print(f'{Cores.bold}{Cores.yellow}           '
          f'Missão Prática Nível 3 - Conjunto das Partes '
          f'{Cores.endColor}{Cores.endColor}')
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    while resposta not in 'nN':
        tamanho_conjunto += 1
        lista_elementos.append(input(f'Digite o {Cores.red}{tamanho_conjunto}º{Cores.endColor} elemento do conjunto: '))
        resposta = input(f'Deseja continuar adicionando elementos? {Cores.red}(Ss/Nn){Cores.endColor}: ')
    lista_elementos = list(set(lista_elementos))
    return sorted(lista_elementos)


if __name__ == '__main__':
    try:
        exibe_conjuntos(dados_entrada())
    except:
        print('Erro ao calcular partes do conjunto!')
