from tkinter import *

#Função para soma
def soma():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())
    soma = valor1 + valor2

#função para verificar se o número é inteiro, e o retorna sem decimal
    if soma.is_integer():
        resultado['text'] = (f'O resultado da sua soma é {int(soma)}')
    else:
        resultado['text'] = (f'O resultado da sua soma é {soma}')

#função para multiplicação
def multiplicacao():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())
    multiplicacao = valor1 * valor2

#Função para verificar se o numero é inteiro, e o retorna sem decimal
    if multiplicacao.is_integer():
        resultado['text'] = (f'O resultado da sua soma é {int(multiplicacao)}')
    else:
        resultado['text'] = (f'O resultado da sua soma é {multiplicacao}')

#função de subtração
def subtracao():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())
    subtracao = valor1 - valor2

#Função para verificar se o numero é inteiro, e o retorna sem decimal
    if subtracao.is_integer():
        resultado['text'] = (f'O resultado da sua soma é {int(subtracao)}')
    else:
        resultado['text'] = (f'O resultado da sua soma é {subtracao}')

#Função de divisão
def divisao():
    valor1 = float(entrada1.get())
    valor2 = float(entrada2.get())

    if valor2 == 0:
        resultado['text'] = (f'Não é possivel dividir por 0')
    divisao = valor1 / valor2

#Função para verificar se o numero é inteiro, e o retorna sem decimal
    if divisao.is_integer():
        resultado['text'] = (f'O resultado da sua soma é {int(divisao)}')
    else:
        resultado['text'] = (f'O resultado da sua soma é {divisao}')

#Criação da inteface
janela = Tk()

janela.title('Calculadora')

texto_orientação = Label(janela, text='Digite nos espaços os números da sua operação')
texto_orientação.grid(column=0, row=0)

#entrada de dados
entrada1 = Entry(janela)
entrada1.grid(column = 0, row= 1, padx= 3, pady=3)

entrada2 = Entry(janela)
entrada2.grid(column= 0, row=2, padx=3, pady =3)

#texto de orientação 2
texto_operacao = Label(janela, text='Selecione abaixo o botão da operação que deseja')
texto_operacao.grid(column=0, row=3, padx=3, pady=3)

#botões das operações

botao_soma = Button(janela, text='+', command=soma)
botao_soma.place(x=90, y=93)

botao_multiplicacao = Button(janela, text='*', command= multiplicacao)
botao_multiplicacao.place(x=115, y=93)

botao_subtracao = Button(janela, text='-', command=subtracao)
botao_subtracao.place(x=140, y=93)

botao_divisao = Button(janela, text='/', command=divisao)
botao_divisao.place(x=165, y=93)

resultado = Label(janela, text='')
resultado.grid(column=0, row=5, padx=25, pady=25)

#impede que a janela feche
janela.mainloop()
