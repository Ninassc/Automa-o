# projeto automação
import pyautogui 
import time
pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)

pyautogui.click(x=685, y=478)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(2)

pyautogui.press('tab')
pyautogui.write('ninasepulveda2009@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(1)

import pandas 
tabela = pandas.read_csv('produto.csv')
for linha in tabela.index:
    pyautogui.click(x=578, y=289)
    codigo = str(tabela.loc[linha, 'codigo'])
    pyautogui.write(codigo) 
    pyautogui.press('tab') 
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo) 
    pyautogui.press('tab')
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria) 
    pyautogui.press('tab')  
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario) 
    pyautogui.press('tab') 
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo) 
    pyautogui.press('tab')
    obs = str(tabela.loc[linha, 'obs']) 
    if obs != 'nan':
        pyautogui.write(obs)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.scroll(50000)
    time.sleep(3)  