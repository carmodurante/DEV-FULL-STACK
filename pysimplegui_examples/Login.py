import PySimpleGUI as sg

## Barra de Progresso
def progress_bar():
    sg.theme('Black')
    layout = [[sg.Text('Criando sua conta...')],
              [sg.ProgressBar(1800, orientation='h', size=(30, 30), key='progbar')],
              [sg.Cancel()]]

    window = sg.Window('Cadastrando...', layout)
    for i in range(1800):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()


## Salvar Usuário em arquivo
def salvar_novo_usuario(username, password, email, admin):
    with open("usuarios.txt", "a") as arquivo_usuarios:
        usuario = [f'\n{username}', f';{password}', f';{email}', f';{admin}']
        arquivo_usuarios.writelines(usuario)


## Carregar Usuários
def carregar_usuarios(username, password):
    lista_usuarios = []
    validado = False
    with open("usuarios.txt", "r") as arquivo_usuarios:
        for linha in arquivo_usuarios:
            linha_limpa = linha.strip()
            lista_split = linha_limpa.split(';')
            lista_usuarios.append(lista_split)

    for linha in lista_usuarios:
        if username == linha[0] and password == linha[1]:
            validado = True

    return validado


## Criar Conta
def create_account():
    sg.theme('Black')
    layout = [[sg.T("Cadastrar Usuário", size=(18, 1), font=40, justification='c', expand_x=True, border_width=10,
                    background_color='White', text_color='Black')],
              [sg.Text("E-mail", size=(19, 1), font=16), sg.InputText(key='EmailCadastro', font=16)],
              [sg.Text("Criar Usuário", size=(19, 1), font=16), sg.InputText(key='UsernameCadastro', font=16)],
              [sg.Text("Criar Senha", size=(19, 1), font=16),
               sg.InputText(key='PasswordCadastro', font=16, password_char='*')],
              [sg.Text('Usuário Administrador?', size=(19, 1), font=16),
               sg.Checkbox('', key='AdminCadastro', default=True, font=16, size=(15, 1))],
              [sg.Button("Cadastrar", pad=(35, 20), key='SubmitCadastro', expand_x=True),
               sg.Button("Cancelar", pad=(35, 20), key='CancelCadastro', expand_x=True)]]

    window = sg.Window("Cadastrar novo usuário", layout)

    while True:
        event, values = window.read()
        if event == 'CancelCadastro' or event == sg.WIN_CLOSED:
            break
        else:
            print(event)
            if event == "SubmitCadastro":
                try:
                    password = values['PasswordCadastro']
                    username = values['UsernameCadastro']
                    admin = values['AdminCadastro']
                    email = values['EmailCadastro']
                    if password.strip() != "" and username.strip() != "":
                        salvar_novo_usuario(username, password, email, admin)
                        progress_bar()
                        break
                    else:
                        sg.popup("Usuario e Senha são Obrigatórios", title='Error', font=8)

                except:
                    sg.popup("Operação Cancelada", title='Error', font=8)
    window.close()


## Logar
def login():
    sg.theme("Black")

    layout = [[sg.T("Log In", size=(18, 1), font=40, justification='c', expand_x=True, border_width=5,
                    background_color='White', text_color='Black')],
              [sg.Text("Usuário:", size=(8, 1), font=16), sg.InputText(key='UsernameLogin', font=16)],
              [sg.Text("Senha:", size=(8, 1), font=16), sg.InputText(key='PasswordLogin', password_char='*', font=16)],
              [sg.Button("Log In", pad=(10, 20), key='SubmitLogin', auto_size_button=True, expand_x=True),
               sg.Button("Cancelar", pad=(10, 20), key='CancelLogin', auto_size_button=True, expand_x=True),
               sg.Button("Cadastrar", pad=(10, 20), key='CadastrarUsuario', auto_size_button=True, expand_x=True)]]

    window = sg.Window("Log In", layout)
    logado = False

    while True:
        try:
            event, values = window.read()
            if event == "CancelLogin" or event == sg.WIN_CLOSED:
                break
            else:
                if event == "SubmitLogin":
                    if carregar_usuarios(values['UsernameLogin'], values['PasswordLogin']) == True:
                        print('logado')
                        logado = True
                        break
                    else:
                        sg.popup("Login inválido", title='Erro Log In', font=8,)

                elif event == 'CadastrarUsuario':
                    create_account()
        except:
            sg.popup("Preencha todos os campos!", title='Error', font=8)

    window.close()
    return logado, admin, window

if __name__ == '__main__':
    try:
        logado, admin, window = login()
    except:
        print('Erro')
