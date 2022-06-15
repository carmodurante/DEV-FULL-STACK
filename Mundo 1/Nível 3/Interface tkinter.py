import tkinter
from tkinter import Button, Entry, Label, messagebox, PhotoImage
import imc_funcoes


def acao():
    indice = imc_funcoes.calcula_imc(peso=peso.get(), altura=altura.get())
    classificacao = imc_funcoes.classifica_imc(indice)
    msg = messagebox.showinfo("Classificação IMC: ", classificacao)



principal = tkinter.Tk()

# Logo
imagem = PhotoImage(file="logo.PNG")
logo = Label(principal, image=imagem)
logo.image = imagem
logo.grid(row=0, column=0, rowspan=2)  # Ocupa 2 linhas

# Etiqueta e caixa de entrada da Altura
etiqueta_altura = Label(principal, text='Altura: ')
etiqueta_altura.grid(row=0, column=1)

altura = Entry(principal)
altura.grid(row=0, column=2)

# Etiqueta e caixa de entrada do Peso
etiqueta_peso = Label(principal, text='Peso: ')
etiqueta_peso.grid(row=1, column=1)

peso = Entry(principal)
peso.grid(row=1, column=2)

# Botão para Calcular IMC
botao = Button(principal, text='Calcular IMC', command=acao)  # Botão que dispara a função acao ao click
botao.grid(row=2, column=2)

principal.mainloop()

