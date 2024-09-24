import PySimpleGUI as sg

# Definindo as cores
BUTTON_COLOR = ('white', '#404040')  # Texto branco com fundo cinza escuro
BACKGROUND_COLOR = '#2b2b2b'  # Fundo da calculadora

# Layout da interface
layout = [
    [sg.Text('', size=(15, 1), justification='right', font=('Arial', 24), key='-DISPLAY-', background_color=BACKGROUND_COLOR, text_color='white')],
    [sg.Button('7', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('8', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('9', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('/', size=(5, 2), button_color=BUTTON_COLOR)],
    [sg.Button('4', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('5', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('6', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('*', size=(5, 2), button_color=BUTTON_COLOR)],
    [sg.Button('1', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('2', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('3', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('-', size=(5, 2), button_color=BUTTON_COLOR)],
    [sg.Button('0', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('.', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('C', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('+', size=(5, 2), button_color=BUTTON_COLOR)],
    [sg.Button('Backspace', size=(5, 2), button_color=BUTTON_COLOR), sg.Button('=', size=(10, 2), button_color=BUTTON_COLOR), sg.Button('Histórico', size=(10, 2), button_color=BUTTON_COLOR)],
]

# Criando a janela
window = sg.Window('CalcPro', layout, background_color=BACKGROUND_COLOR)

# Variáveis de controle
current_input = ''
full_expression = ''
history = []

# Loop principal da aplicação
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in '0123456789':
        current_input += event
        window['-DISPLAY-'].update(current_input)

    if event in '/*-+':
        full_expression += current_input + event
        current_input = ''
        window['-DISPLAY-'].update(event)

    if event == '.':
        if '.' not in current_input:
            current_input += event
            window['-DISPLAY-'].update(current_input)

    if event == 'C':
        current_input = ''
        full_expression = ''
        window['-DISPLAY-'].update(current_input)

    if event == 'Backspace':
        current_input = current_input[:-1]
        window['-DISPLAY-'].update(current_input)

    if event == '=':
        full_expression += current_input
        try:
            result = str(eval(full_expression))
            history.append(full_expression + ' = ' + result)
            window['-DISPLAY-'].update(result)
            current_input = result
            full_expression = ''
        except:
            window['-DISPLAY-'].update('Error')
            current_input = ''
            full_expression = ''

    if event == 'Histórico':
        history_display = '\n'.join(history[-10:])  # Mostra os últimos 10 cálculos
        sg.popup('Histórico de Operações', history_display, background_color=BACKGROUND_COLOR, text_color='white')

window.close()
