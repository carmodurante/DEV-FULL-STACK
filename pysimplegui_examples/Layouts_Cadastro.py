import PySimpleGUI as sg


def layout_cadastro(lista_cadastrado_ferramentas, lista_cadastrado_tecnicos, lista_cadastrado_reservas):

    ############ Define Layout Cadastro Ferramentas ############
    header_cadastro_ferramentas = ['ID Ferramenta', 'Descrição', 'Fabricante', 'Voltagem', 'Cód. Fabricante',
                                   'Tamanho', 'Unidade Medida', 'Material', 'Tempo Max Reserva', 'Reservado?']

    buttons_cadastro_ferramentas = [[sg.Button('Cadastrar', key='CadastrarFerramenta', pad=(15, 7)),
                                     sg.Button('Modificar', key='ModificarFerramenta', pad=(15, 7)),
                                     sg.Button('Eliminar', key='EliminarFerramenta', pad=(15, 7))]]

    layout_cad_ferramentas = [[sg.Text('Descrição', size=(18, 1)), sg.Input('', key='fDescricao'),
                               sg.Text('Nome do Fabricante', size=(18, 1)), sg.Input('', key='fFabricante')],
                              [sg.Text('Voltagem de Uso', size=(18, 1)),
                               sg.Combo(['220V', '110V', 'N/D'], default_value='110V', key='fVoltagem', size=43),
                               sg.Text('Código no Fabricante', size=(18, 1)), sg.Input('', key='eEmail')],
                              [sg.Text('Tamanho', size=(18, 1)), sg.Input('', key='fTamanho'),  # Listbox
                               sg.Text('Unidade de Medida', size=(18, 1)), sg.Input('', key='fUnidade')],  # Listbox
                              [sg.Text('Tipo da Ferramenta', size=(18, 1)), sg.Input('', key='fTipo'),  # Listbox
                               sg.Text('Material da Ferramenta', size=(18, 1)), sg.Input('', key='fMaterial')],
                              # Listbox
                              [sg.Text('Tempo Max. de Reserva', size=(18, 1)),
                               sg.Input('', key='fTempoReserva', size=6, ),
                               sg.Text('(Horas)', size=(7, 1))],
                              [sg.Frame('Opções de Cadastro de Ferramentas', layout=buttons_cadastro_ferramentas,
                                        element_justification='left', expand_x=True, pad=(10, 10))],
                              [sg.Table(values=lista_cadastrado_ferramentas,
                                        headings=header_cadastro_ferramentas,
                                        max_col_width=35,
                                        auto_size_columns=True,
                                        display_row_numbers=True,
                                        justification='left',
                                        num_rows=6,
                                        key='-TABLE_CAD_FERRAMENTAS-',
                                        row_height=35,
                                        enable_click_events=True,
                                        vertical_scroll_only=False)]]

    ############ Define Layout Cadastro Tecnicos ############
    header_cadastro_tecnicos = ['CPF', 'Nome Técnico', 'Telefone/Celular', 'Turno/Período', 'Nome da Equipe']

    buttons_cadastro_tecnico = [[sg.Button('Cadastrar', key='CadastrarTecnico'),
                                 sg.Button('Modificar', key='ModificarTecnico'),
                                 sg.Button('Eliminar', key='EliminarTecnico')]]

    layout_cad_tecnico = [[sg.Text('CPF', size=(18, 1)), sg.Input('', key='tCPF')],
                          [sg.Text('Nome', size=(18, 1)), sg.Input('', key='tNome')],
                          [sg.Text('Telefone', size=(18, 1)), sg.Input('', key='tTelefone')],
                          [sg.Text('Turno', size=(18, 1)), sg.Combo(['Manhã', 'Tarde', 'Noite'],
                                                                    default_value='Manhã', key='fTurno', size=43)],
                          [sg.Text('Nome da Equipe', size=(18, 1)), sg.Input('', key='tEquipe')],
                          [sg.Frame('Opções de Cadastro de Técnicos', layout=buttons_cadastro_tecnico,
                                    element_justification='left', expand_x=True, pad=(10, 10))],
                          [sg.Table(values=lista_cadastrado_tecnicos,
                                    headings=header_cadastro_tecnicos,
                                    max_col_width=35,
                                    auto_size_columns=True,
                                    display_row_numbers=True,
                                    justification='left',
                                    num_rows=6,
                                    key='-TABLE_CAD_TECNICOS-',
                                    row_height=35,
                                    enable_click_events=True)]]

    ############ Define Layout Cadastro Reservas ############

    layout_cad_reserva = [[sg.Text('Last Job', size=(10, 1)), sg.Input('', key='eLastJ')],
                          [sg.Text('From Date', size=(10, 1)), sg.Input('', key='eJFdt')],
                          [sg.Text('To Date', size=(10, 1)), sg.Input('', key='eJTdt')],
                          [sg.Text('Company Name', size=(10, 1)), sg.Input('', key='eLJcmpy')],
                          [sg.Button('Save Experience Details')]]

    # Define o TabGroup Cadastro
    tabgrp_cadastro = [[sg.TabGroup([[
        sg.Tab('Cadastro de Ferramentas', layout_cad_ferramentas, border_width=5, element_justification='left'),
        sg.Tab('Cadastro de Técnicos      ', layout_cad_tecnico, border_width=5, element_justification='left'),
        sg.Tab('Cadastro de Reservas     ', layout_cad_reserva, border_width=5, element_justification='left')
    ]], tab_location=sg.TAB_LOCATION_TOP_LEFT, border_width=7, font='_ 12')]]

    return tabgrp_cadastro