from deep_translator import GoogleTranslator  
import PySimpleGUI as sg   

sg.theme('Topanga')  

tradutor = GoogleTranslator(source='portuguese', target="en")  

layout = [ 
    [sg.Text("Translate")],  
    [sg.Text("Texto para traduzir:", size=(15, 1)), sg.InputText(key='-TEXTO-')],  
    [sg.Button('Traduzir'), sg.Button('Sair', key='-SAIR')],  
    [sg.Text('Tradução:', size=(15, 1)), sg.Text(size=(40, 1), key='-TRADUCAO-')] 
]

window = sg.Window('Tradutor', layout) 


while True:  
    event, values = window.read()  
    
    if event == sg.WIN_CLOSED or event == "-SAIR":  
        break  
    
    if event == 'Traduzir':  
        texto = values['-TEXTO-']  
        
        try:  
            traducao = tradutor.translate(texto)  
            window['-TRADUCAO-'].update(traducao)  
            window['-TEXTO-'].update('')  # Limpa o campo de entrada  
        except Exception as e:  
            window['-TRADUCAO-'].update(f"Erro na tradução: {str(e)}")  
    
window.close()  