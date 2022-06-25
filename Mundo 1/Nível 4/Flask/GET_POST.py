from flask import Flask
from flask import request

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return "Página principal."

    @app.route('/ola/')
    @app.route('/ola/<nome>')
    def ola_mundo(nome):
        return "Olá, " + nome

    @app.route('/logar', methods=['GET', 'POST'])
    def logar():
        if request.method == 'POST':
            return "Recebeu post! Fazer login!"
        else:
            return "Recebeu get! Exibir FORM de login."


if __name__ == '__main__':
    app.run()
