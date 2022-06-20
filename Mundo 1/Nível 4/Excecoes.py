from logging import exception


class ExcecaoCustomizada(exception):
    pass

    def throws(self):
        raise ExcecaoCustomizada


try:
    ExcecaoCustomizada.throws()
except ExcecaoCustomizada as ex:
    print("Excecao lançada!")
