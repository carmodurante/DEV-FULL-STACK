# Personalizando o retorno do logging
import logging


dados = {'pessoa': 'jess'}


def outro_log():
    logging.debug("Esta é uma mensagem de debug", extra=dados)


def main():
    # Defina o nível de log para debug e um arquivo para salvar 
    # o retorno. Use também uma formatação personalizada
    formato = ("%(asctime)s: %(levelname)s: %(funcName)s "
               "Linha:%(lineno)d Pessoa:%(pessoa)s %(message)s")

    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=formato)

    logging.info("Esta é uma mensagem de informação", extra=dados)
    logging.warning("Esta é uma mensagem de aviso", extra=dados)
    outro_log()


if __name__ == "__main__":
    main()
