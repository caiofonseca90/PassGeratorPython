import os
from random import random
import time
from typing import Text
import PySimpleGUI as sg
import random
import string


def tela():
    # 1 - criar o tema para a janela
    sg.theme('DarkAmber')
    # 1.2 - criar os elementos da janela
    layout =[ 
            [sg.Input('Senha',size=(20,2),justification='center'),sg.Combo(values=list(range(31)))],
            [sg.Input('E-mail', size=(60,1),justification='center')],
            [sg.Button('Gerar', size=(6,1))],  [sg.Button('Enviar', size=(6,1))]
            ]
    # 1.2 - criar a janela
    janela = sg.Window('Gerador de Senha',layout, element_justification='center')
    # 1.3 criar os eventos da janela
    while True:
        eventos, valores = janela.read()
        if eventos == sg.WIN_CLOSED:
            break
        
    
    janela.close()  





tela()