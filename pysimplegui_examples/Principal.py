import PySimpleGUI as sg

from Layouts_Cadastro import layout_cadastro
from Layouts_Consulta import layout_consulta

# Define o tema
sg.theme('Black')

########## Dados Tabelas ##########
lista_cadastrado_ferramentas = [['1001', 'Chave Inglesa', 'John Deere', '110V', '1015-U521', '10', 'Polegadas',
                                 'Metal', '36', 'True'],
                                ['1002', 'Chave de Fenda', 'John Deere', 'N/D', '1015-U522', '40', 'Metros',
                                 'Aluminio', '24', 'False']
                                ]

lista_cadastrado_tecnicos = [['46794179865', 'Carmo Durante Neto', '16992180889', 'Manhã', 'Hell Fire'],
                             ['12345678910', 'Jose Carlos', '1699111111', 'Noite', 'Titans']]

lista_cadastrado_reservas = []

########## Definição de TabGroups ##########
tabgrp_cadastro = layout_cadastro(lista_cadastrado_ferramentas, lista_cadastrado_tecnicos, lista_cadastrado_reservas)
tabgrp_consulta = layout_consulta()

########## Definição Tela Principal ##########
tabgroup_menu = [
    # Dados Cabeçalho
    [sg.T('Central de Ferramentaria AudioVisual', font='_ 16', justification='c', expand_x=True,
          border_width=10, background_color='white', text_color='black')],
    # Dados TabGroup Principal
    [sg.TabGroup([[
        sg.Tab('Cadastros', tabgrp_cadastro, border_width=5, element_justification='left'),
        sg.Tab('Consultas', tabgrp_consulta, border_width=5, element_justification='left')]],
        tab_location=sg.TAB_LOCATION_TOP, border_width=12, font='_ 12')],
    # Dados Footer
    [sg.Text('Usuário Logado:', size=(12, 1)),
     sg.Text('CarmoDurante', size=(18, 1), text_color='green'),
     sg.Text('Admin: ', size=(5, 1)), sg.Text('False', size=(18, 1), text_color='red')]]

# Define Window
window = sg.Window('App Central de Ferramentaria AudioVisual', tabgroup_menu, resizable=True)

while True:
    # Read values entered by user
    try:
        event, values = window.read()
    except:
        break
    print(event)
    if event == sg.WIN_CLOSED:  # always, always give a way out!
        break
