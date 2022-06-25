from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Página principal."


@app.route('/ola')
def ola_mundo():
    return "Olá, mundo."


if __name__ == '__main__':
    app.run()
