import tkinter as tk
from tkinter import Label, Entry, Frame, Button



#### CALCULADORA ####
def calc():
    global imc
    imc = float(peso.get()) / float(altura.get())  ** 2
    if imc < 18.5:
        result = 'Abaixo do normal'
    elif 18.5 < imc <= 24.9:
        result = 'Normal'
    elif 25 < imc <= 29.9:
        result = 'Sobrepeso'
    elif 30 < imc <= 34.9:
        result = 'Obesidade grau 1'
    elif 35 < imc <= 39.9:
        result = 'Obesidade grau 2'
    else:
        result = 'Obesidade grau 3'
    resultado['text'] = f'Seu IMC é {imc} - {result}'
    print(f'Seu IMC é {imc}')
#####################



janela = tk.Tk()

frame = Frame(janela, padx=40, pady=40).grid(column=1, row=1)
Label(frame, text='Insira as informações abaixo para saber seu IMC', pady=40).grid(column=1, row=1, columnspan=2)

Label(frame, text='Seu peso(kg):').grid(column=1, row=2)
Label(frame, text='Sua altura (m):').grid(column=1, row=3)

peso = Entry(frame)
peso.grid(column=2, row=2)
altura = Entry(frame)
altura.grid(column=2, row=3)


Button(frame, text='Calcular', command=calc).grid(column=3, row=4)
resultado = Label(frame)
resultado.grid(column=1, row=5, columnspan=2)

janela.title('Calculadora IMC')
janela.mainloop()