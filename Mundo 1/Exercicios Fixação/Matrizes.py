def mult_matrizes(A, B):
    nLinhasA = len(A)
    nColunasA = len(A[0])
    nColunasB = len(B[0])

    M = []

    for linha in range(nLinhasA):
        ##Començando a linha nova em M
        M.append([])
        for coluna in range(nColunasB):
            M[linha].append(0)
            for k in range(nColunasA):
                M[linha][coluna] += A[linha][k] * B[k][coluna]

    return M


A = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
B = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

print(mult_matrizes(A, B))
