from tkinter import *

#função que chama a função de calcular
def calcularimc():

    #recebe a entrada do usuario e converte
    cm = float(entrada_altura.get())
    peso = float(entrada_peso.get())

    #Transformando cm em metros
    altura = cm / 100
    
    #calculo do imc
    imc = peso / (altura * 2)

    if imc <= 18.5:
        resultado['text']= f'Você está abaixo do peso, seu IMC é: {imc:.2f}'
    elif 18.5 < imc < 24.9:
        resultado['text']= f'Você está com o peso normal, seu IMC é: {imc:.2f}'    
    elif 25.0 < imc < 29.99:
        resultado['text']= f'Você está com o sobrepeso, seu IMC é: {imc:.2f}'
    elif imc > 30.0:
        resultado['text']= f'CUIDADO, Você está com o Obesidade, seu IMC é: {imc:.2f}'



    

janela = Tk()

janela.title('Calculadora de IMC')
janela.configure(background='lightblue')

texto_orientacao = Label(janela, text='Sejá bem-vindo, nós informe os requisitos solicitados a baixo com precisão', font=('Arial', 12, 'bold'))
texto_orientacao.grid(column=0, row=1)

texto_altura = Label(janela, text='Digite sua altura em CM, no espaço a baixo', font=('Arial', 12))
texto_altura.place(x=130, y=30)

entrada_altura = Entry(janela)
entrada_altura.place(x=140, y=60)

texto_peso = Label(janela, text='Digite seu peso, no espaço a baixo, se necessário use "."', font=('Arial', 12))
texto_peso.place(x=130, y=90)

entrada_peso = Entry(janela)
entrada_peso.place(x=140, y=120)

botao_resultado = Button(text='Resultado', command=calcularimc)
botao_resultado.place(x=140, y= 150)

resultado = Label(janela, text='', font=('Arial', 12, 'bold'))
resultado.place(x=130, y=190)

janela.geometry('580x260')



janela.mainloop()





 



