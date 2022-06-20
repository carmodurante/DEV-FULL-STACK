from logging import exception


class ExcecaoCustomizada(exception):
    pass

    def throws(self):
        raise ExcecaoCustomizada


try:
    exception = ExcecaoCustomizada()
    ExcecaoCustomizada.throws(self=exception)
except ExcecaoCustomizada as ex:
    print("Excecao lançada!")
