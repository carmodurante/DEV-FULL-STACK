# Deques são filas duplamente terminadas
import collections
import string


def main():
    # Inicialize um deque com letras minúsculas
    letrinhas = collections.deque(string.ascii_lowercase)

    # Deques suportam o método len(), mostre o tamanho da deque
    print("Item count: {}".format(str(len(letrinhas))))

    # Itere sobre a deque criada
    for letra in letrinhas:
        print(letra.upper(), end=",")

    # Manipule os itens em qualquer um dos terminais
    letrinhas.pop()
    letrinhas.popleft()
    letrinhas.append(2)
    letrinhas.appendleft(1)
    print(letrinhas)

    # Rotacione a deque
    print(letrinhas)
    letrinhas.rotate(10)
    print(letrinhas)


if __name__ == "__main__":
    main()
