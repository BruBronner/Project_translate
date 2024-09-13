from deep_translator import GoogleTranslator
import PySimpleGUI as sg 

#tema PySimpleGUI
sg.theme('topanga')



tradutor = GoogleTranslator(source= 'portuguese', target = "en")

#layout da ´pagine
layout = [[sg.Text("Transcrição de vídeo")],
          [sg.InputText('URL:', key='-TEXTO-')],
          [sg.Button('Translate'), sg.Button('Sair', key='-SAIR')],
          [sg.Text('Tradução:', size=(15,1)), sg.Text(size=(40,1), key= '-TRADUCAO-')]]

window = sg.Window('Tradutor', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "-SAIR":
        break
    
    if event == 'Translate':
        texto = values['-TEXTO-']
        
        try:
            traducao = tradutor.translate(texto)
            window['-TRADUCAO-'].update(traducao)
        except Exception as e:
            window['-TRADUCAO-'].update("erro na tradução")
    
     
        
    else:
            ...
    
    
            
window.close()






