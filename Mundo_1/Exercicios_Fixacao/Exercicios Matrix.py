from numpy import array


cadeiras = array([["Português", "Matemática", "Química"], ["História", "Geografia", "Física"]], dtype=str)
cadeiras2 = array(["Português", "Matemática", "Química"], dtype=str)
cadeiras[1][2] = 'Cálculo'
cadeiras2[2] = 'Cálculo'
print(cadeiras[1][2])
print(cadeiras2[2])