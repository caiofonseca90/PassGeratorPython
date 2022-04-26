import os
from random import random
import time
from typing import Text
import PySimpleGUI as sg
import random
import string


#função senha
def senha():
#definindo as variaveis
    mi = string.ascii_lowercase
    ma = string.ascii_uppercase
    di = string.digits
    si = string.punctuation
#Agregado dos caracteres     
    tudo = mi + ma + di + si
#definindo tamanho da senha
    tam6 = 6
    tam8 = 6
    tam14 = 14
    tam16 = 16
#definindo como sera feita a senha
    senha = ''.join(random.sample( tudo, tam6)).strip()
    print('\nA senha gerada é: {}  \n'.format(senha))



senha()

time.sleep(10)
os.system('cls')