import PySimpleGUI as sg


def layout_consulta():
    ############ Define Layout Consulta Ferramentas ############
    layout_con_ferramentas = [[sg.Text('Name', size=(10, 1)), sg.Input('', key='eName')],
                              [sg.Text('Date of Birth', size=(10, 1)), sg.Input('', key='eDob')],
                              [sg.Text('Phone No', size=(10, 1)), sg.Input('', key='ePhone')],
                              [sg.Text('Email ID', size=(10, 1)), sg.Input('', key='eEmail')],
                              [sg.Button('Save Personal Details')]]

    ############ Define Layout Consulta Tecnicos ############
    layout_con_tecnico = [[sg.Text('Highest Qualfication', size=(15, 1)), sg.Input('', key='eQual')],
                          [sg.Text('Year of Qualifying', size=(15, 1)), sg.Input('', key='eYoq')],
                          [sg.Text('Grade', size=(15, 1)), sg.Input('', key='eGrade')],
                          [sg.Text('University/College', size=(15, 1)), sg.Input('', key='eQUniv')],
                          [sg.Button('Save Education Details')]]

    ############ Define Layout Consulta Reservas ############
    layout_con_reserva = [[sg.Text('Last Job', size=(10, 1)), sg.Input('', key='eLastJ')],
                          [sg.Text('From Date', size=(10, 1)), sg.Input('', key='eJFdt')],
                          [sg.Text('To Date', size=(10, 1)), sg.Input('', key='eJTdt')],
                          [sg.Text('Company Name', size=(10, 1)), sg.Input('', key='eLJcmpy')],
                          [sg.Button('Save Experience Details')]]

    # Define o TabGroup Consulta
    tabgrp_consulta = [[sg.TabGroup([[
        sg.Tab('Consulta de Ferramentas', layout_con_ferramentas, border_width=5, element_justification='left'),
        sg.Tab('Consulta de Técnicos     ', layout_con_tecnico, border_width=5, element_justification='left'),
        sg.Tab('Consulta de Reservas     ', layout_con_reserva, border_width=5, element_justification='left')
    ]], tab_location=sg.TAB_LOCATION_TOP_LEFT, border_width=7, font='_ 12')]]

    return tabgrp_consulta