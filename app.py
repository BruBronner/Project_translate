from deep_translator import GoogleTranslator  
import PySimpleGUI as sg  


sg.theme('DarkGreen7')
layout = [  
    [sg.Text("Tradutor", font=("Helvetica", 16), justification='center', pad=(10, 10))],  
    [sg.Text("Digite a frase:", font=("Helvetica", 12), pad=(10, 5))],  
    [sg.InputText('', key='-TEXTO-', size=(50, 1), pad=(10, 5))],  
    [sg.Button('Traduzir', size=(10, 1), pad=(10, 5)), sg.Button('Sair', size=(10, 1), key='-SAIR', pad=(10, 5))],  
    [sg.Text('Tradução:', font=("Helvetica", 12), pad=(10, 5)), sg.Text(size=(40, 1), key='-TRADUCAO-', font=("Helvetica", 12), pad=(10, 5))]  
]  
window = sg.Window("Tradutor", layout, element_justification='c', finalize=True)  


def traduzir(texto):  
    try:  
        if texto.strip():  # Verifica se o texto não está vazio  
            return GoogleTranslator(source='auto', target='pt').translate(texto)  
        return "Por favor, insira um texto para traduzir."  
    except Exception as e:  
        return "Erro na tradução: " + str(e)  

while True:  
    event, values = window.read()  
    if event in (sg.WIN_CLOSED, '-SAIR'):  
        break  
    if event == 'Traduzir':  
        texto = values['-TEXTO-']  
        traducao = traduzir(texto)  
        window['-TRADUCAO-'].update(traducao)  


window.close()  