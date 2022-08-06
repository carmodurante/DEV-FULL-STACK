# Uso do módulo logging

# Use o módulo embutido logging
import logging


def main():
    # Use basicConfig para configurar seu logging
    # Lembrete: essa parte só é executada uma vez, chamadas
    # subsequentes não terão efeito
    logging.basicConfig(level=logging.DEBUG,
                        filemode="w",
                        filename="output.log")

    # Testando cada um dos níveis de log
    logging.debug("Esta é uma mensagem de debug")
    logging.info("Esta é uma mensagem de informação")
    logging.warning("Esta é uma mensagem de aviso")
    logging.error("Esta é uma mensagem de erro")
    logging.critical("Esta é uma mensagem crítica")

    # Use strings para formatar o log
    logging.info("Aqui temos uma variável {} e um int: {}".format("string", 10))


if __name__ == "__main__":
    main()
