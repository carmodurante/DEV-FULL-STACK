#minha_string = f"Olá Mundo {expr}"
from datetime import datetime

frutas = ['jabuticaba', 'laranja', 'uva', 'banana']
for fruta in frutas:
    # Padrão — varivel: numero_de_espacos
    minha_fruta = f"Nome: {fruta:11} - Número de letras: {len(fruta):2}"
    print(minha_fruta)

print()

pi = 3.1415
#{variavel_float:largura.precisao f}
meu_numero = f'O número PI é: {pi:.2f}'
meu_numero_deslocado = f'O número PI deslocado é: {pi:6.1f}'
meu_numero_preciso = f'O número PI mais preciso é: {pi:.4f}'
print(meu_numero)
print(meu_numero_deslocado)
print(meu_numero_preciso)

print()

data = datetime.now()
minha_data = f'A data de hoje é {data}'
minha_data_formatada = f'A data de hoje formatada é {data:%d/%m/%Y}'
print(minha_data)
print(minha_data_formatada)