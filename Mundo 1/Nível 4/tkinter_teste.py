import tkinter as tk

contador = 0


def contador_label(lblRotulo):
    global contador
    print(contador)
    contador = contador + 1
    lblRotulo.config(text=str(contador))
    # lblRotulo.after(1000, funcao_contar())
    contador_label(lblRotulo)


janela = tk.Tk()

janela.title("Contagem dos Segundos")

lblRotulo = tk.Label(janela, fg="green", text=contador)
lblRotulo.pack()

contador_label(lblRotulo)

btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
btnAcao.pack()

janela.mainloop()

contador_label(lblRotulo)