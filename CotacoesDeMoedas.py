import requests
import json
from tkinter import *

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

def cotacoes_chamar():

    cotacao_dolar = cotacoes['USDBRL']['bid']
    cotacao_euro = cotacoes['EURBRL']['bid']
    cotacao_btc = cotacoes ['BTCBRL']['bid']

    cotacoes_resu['text'] = (f'''
    DOLAR : R$ {cotacao_dolar}
    EURO  : R$ {cotacao_euro}
    BTC   : R$ {cotacao_btc} ''')



janela = Tk()

janela.title('Cotações de Moedas')
janela.configure(background='lightblue')

texto_orientacao = Label(janela, text='Por favor, clique no botão abaixo para visualizar as cotações atualizadas das moedas.')
texto_orientacao.grid(column=0, row=1)

botao = Button(janela, text='Cotações', command=cotacoes_chamar)
botao.grid(column=0, pady=13)

cotacoes_resu = Label(janela, text='')
cotacoes_resu.configure(background='lightblue')
cotacoes_resu.grid(column=0, pady=1)


janela.mainloop()
