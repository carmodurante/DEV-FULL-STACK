# strings e bytes não são diretamente intercambiáveis
# strings contém unicode, bytes são valores de 8 bits

def main():
    # definindo alguns valores iniciais
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "Isto é uma string"
    print(s)

    # Tente combinar os dois. A linha abaixo vai mostrar um erro:
    # print(s + b)

    # Bytes e strings precisam ser apropriadamente encoded e
    # decoded antes de serem usados em conjunto
    s2 = b.decode('utf-8')
    print(s + s2)

    b2 = s.encode('utf-8')
    print(b + b2)

    # Faça o encode da string como UTF-32
    b3 = s.encode('utf-32')
    print(b3)


if __name__ == "__main__":
    main()
