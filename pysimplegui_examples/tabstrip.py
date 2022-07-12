import PySimpleGUI as sg

# Define o tema
sg.theme('DarkAmber')

# Define Layout Cadastro Ferramentas
buttons_cadastro_ferramentas = [[sg.Button('Buscar',    key='BuscarFerramenta'),
                                 sg.Button('Cadastrar', key='CadastrarFerramenta'),
                                 sg.Button('Modificar', key='ModificarFerramenta'),
                                 sg.Button('Eliminar',  key='EliminarFerramenta')]]

layout_cad_ferramentas = [[sg.Text('Name', size=(10, 1)), sg.Input('', key='eName')],
                         [sg.Text('Date of Birth', size=(10, 1)), sg.Input('', key='eDob')],
                         [sg.Text('Phone No', size=(10, 1)), sg.Input('', key='ePhone')],
                         [sg.Text('Email ID', size=(10, 1)), sg.Input('', key='eEmail')],
                         [sg.Frame('Opções de Cadastro de Ferramentas', layout=buttons_cadastro_ferramentas,
                                   element_justification='center')]]

# Define Layout Cadastro Tecnicos
buttons_cadastro_tecnico = [[sg.Button('Buscar',    key='BuscarTecnico'),
                             sg.Button('Cadastrar', key='CadastrarTecnico'),
                             sg.Button('Modificar', key='ModificarTecnico'),
                             sg.Button('Eliminar',  key='EliminarTecnico')]]

layout_cad_tecnico = [[sg.Text('Highest Qualfication', size=(15, 1)), sg.Input('', key='eQual')],
                      [sg.Text('Year of Qualifying', size=(15, 1)), sg.Input('', key='eYoq')],
                      [sg.Text('Grade', size=(15, 1)), sg.Input('', key='eGrade')],
                      [sg.Text('University/College', size=(15, 1)), sg.Input('', key='eQUniv')],
                      [sg.Frame('Opções de Cadastro de Técnicos', layout=buttons_cadastro_tecnico,
                                element_justification='center')]]

# Define Layout Cadastro Reservas
layout_cad_reserva = [[sg.Text('Last Job', size=(10, 1)), sg.Input('', key='eLastJ')],
                      [sg.Text('From Date', size=(10, 1)), sg.Input('', key='eJFdt')],
                      [sg.Text('To Date', size=(10, 1)), sg.Input('', key='eJTdt')],
                      [sg.Text('Company Name', size=(10, 1)), sg.Input('', key='eLJcmpy')],
                      [sg.Button('Save Experience Details')]]

# Define Layout Consulta Ferran
layout_con_ferramentas = [[sg.Text('Name', size=(10, 1)), sg.Input('', key='eName')],
                          [sg.Text('Date of Birth', size=(10, 1)), sg.Input('', key='eDob')],
                          [sg.Text('Phone No', size=(10, 1)), sg.Input('', key='ePhone')],
                          [sg.Text('Email ID', size=(10, 1)), sg.Input('', key='eEmail')],
                          [sg.Button('Save Personal Details')]]

layout_con_tecnico = [[sg.Text('Highest Qualfication', size=(15, 1)), sg.Input('', key='eQual')],
                      [sg.Text('Year of Qualifying', size=(15, 1)), sg.Input('', key='eYoq')],
                      [sg.Text('Grade', size=(15, 1)), sg.Input('', key='eGrade')],
                      [sg.Text('University/College', size=(15, 1)), sg.Input('', key='eQUniv')],
                      [sg.Button('Save Education Details')]]

layout_con_reserva = [[sg.Text('Last Job', size=(10, 1)), sg.Input('', key='eLastJ')],
                      [sg.Text('From Date', size=(10, 1)), sg.Input('', key='eJFdt')],
                      [sg.Text('To Date', size=(10, 1)), sg.Input('', key='eJTdt')],
                      [sg.Text('Company Name', size=(10, 1)), sg.Input('', key='eLJcmpy')],
                      [sg.Button('Save Experience Details')]]

# Define o TabGroup Cadastro
tabgrp_cadastro = [[sg.TabGroup([[
                   sg.Tab('Cadastro de Ferramentas', layout_cad_ferramentas, border_width=5, element_justification='left'),
                   sg.Tab('Cadastro de Técnicos', layout_cad_tecnico, border_width=5, element_justification='left'),
                   sg.Tab('Cadastro de Reservas', layout_cad_reserva, border_width=5, element_justification='left')
                    ]],tab_location=sg.TAB_LOCATION_LEFT_TOP, border_width=7)]]

# Define o TabGroup Consulta
tabgrp_consulta = [[sg.TabGroup([[
                   sg.Tab('Consulta de Ferramentas', layout_con_ferramentas, border_width=5, element_justification='left'),
                   sg.Tab('Consulta de Técnicos', layout_con_tecnico, border_width=5, element_justification='left'),
                   sg.Tab('Consulta de Reservas', layout_con_reserva, border_width=5, element_justification='left')
                    ]],tab_location=sg.TAB_LOCATION_LEFT_TOP, border_width=7)]]

tabgroup_menu = [[sg.T('Central de Ferramentaria AudioVisual', font='_ 16', justification='c', expand_x=True, border_width=5)],
                 [sg.TabGroup([[
                  sg.Tab('Cadastros', tabgrp_cadastro, border_width=5, element_justification='left'),
                  sg.Tab('Consultas', tabgrp_consulta, border_width=5, element_justification='left')]],
                  tab_location=sg.TAB_LOCATION_TOP, border_width=15)]]

# Define Window
window = sg.Window('App Central de Ferramentaria AudioVisual', tabgroup_menu)

while True:
    # Read values entered by user
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:  # always, always give a way out!
        break
