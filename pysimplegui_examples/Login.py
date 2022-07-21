import PySimpleGUI as sg

username = ''
password = ''


# PROGRESS BAR
def progress_bar():
    sg.theme('Black')
    layout = [[sg.Text('Criando sua conta...')],
              [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
              [sg.Cancel()]]

    window = sg.Window('Trabalhando...', layout)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


def create_account():
    sg.theme('Black')
    layout = [[sg.T("Registrar Usuário", size=(18, 1), font=40, justification='c', expand_x=True, border_width=10,
                    background_color='White', text_color='Black')],
              [sg.Text("E-mail", size=(19, 1), font=16), sg.InputText(key='EmailCadastro', font=16)],
              [sg.Text("Criar Usuário", size=(19, 1), font=16), sg.InputText(key='UsernameCadastro', font=16)],
              [sg.Text("Criar Senha", size=(19, 1), font=16),
               sg.InputText(key='PasswordCadastro', font=16, password_char='*')],
              [sg.Text('Usuário Administrador?', size=(19, 1), font=16),
               sg.Checkbox('', key='Admin', default=True, font=16, size=(15, 1))],
              [sg.Button("Cadastrar", pad=(35, 20), key='SubmitCadastro', auto_size_button=True, expand_x=True),
               sg.Button("Cancelar", pad=(35, 20), key='CancelCadastro', auto_size_button=True, expand_x=True)]]

    window = sg.Window("Cadastrar novo usuário", layout)

    while True:
        event, values = window.read()
        if event == 'CancelCadastro' or event == sg.WIN_CLOSED:
            break
        else:
            if event == "SubmitCadastro":
                password = values['PasswordCadastro']
                username = values['UsernameCadastro']
                progress_bar()
                break
    window.close()


def login():
    global username, password
    sg.theme("Black")
    layout = [[sg.T("Log In", size=(18, 1), font=40, justification='c', expand_x=True, border_width=5,
                    background_color='White', text_color='Black')],
              [sg.Text("Usuário:", size=(8, 1), font=16), sg.InputText(key='UsernameLogin', font=16)],
              [sg.Text("Senha:", size=(8, 1), font=16), sg.InputText(key='PasswordLogin', password_char='*', font=16)],
              [sg.Button("Log In", pad=(10, 20), key='SubmitLogin', auto_size_button=True, expand_x=True),
               sg.Button("Cancelar", pad=(10, 20), key='CancelLogin', auto_size_button=True, expand_x=True),
               sg.Button("Cadastrar", pad=(10, 20), key='CadastrarUsuario', auto_size_button=True, expand_x=True)]]

    window = sg.Window("Log In", layout)

    while True:
        event, values = window.read()
        if event == "CancelLogin" or event == sg.WIN_CLOSED:
            break
        else:
            if event == "SubmitLogin":
                if values['UsernameLogin'] == username and values['PasswordLogin'] == password:

                    break
                elif values['UsernameLogin'] != username or values['PasswordLogin'] != password:
                    sg.popup("Login inválido, tente novamente!")

    window.close()


if __name__ == '__main__':
    create_account()
    login()
