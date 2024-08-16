import PySimpleGUI as sg

# Função para calcular o maior e menor número e contar os valores
def calcular_maior_menor(valores):
    if valores:
        maior = valores[0]
        menor = valores[0]
        for valor in valores[1:]:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
        return maior, menor, len(valores)
    else:
        return None, None, 0

# Paleta de Cores
background_color = '#2E2E2E'  # Fundo escuro
input_background = '#4A4A4A'  # Fundo dos inputs
text_color = '#FFFFFF'        # Texto em branco
button_color = ('#FFFFFF', '#007BFF')  # Texto dos botões em branco e fundo azul
button_color_secondary = ('#FFFFFF', '#4CAF50')  # Texto dos botões secundários em branco e fundo verde
result_color = '#FFD700'      # Amarelo para o resultado

# Layout da janela principal
layout = [
    [sg.Text("Insira valores e clique em 'Adicionar' para adicionar à lista:", font=('Arial', 12), text_color=text_color)],
    [sg.Input(size=(15, 1), key='-VALOR-', font=('Arial', 12), background_color=input_background, text_color=text_color)],
    [sg.Button('Adicionar', button_color=button_color, font=('Arial', 12)), sg.Button('Limpar Lista', button_color=button_color_secondary, font=('Arial', 12))],
    [sg.Text("Valores Adicionados:", font=('Arial', 12), text_color=text_color)],
    [sg.Listbox(values=[], size=(30, 10), key='-LISTA-', font=('Arial', 12), background_color=input_background, text_color=text_color)],
    [sg.Button('Calcular', button_color=button_color, font=('Arial', 12)), sg.Button('Sair', button_color=button_color_secondary, font=('Arial', 12))],
    [sg.Text('', size=(40, 3), key='-RESULTADO-', font=('Arial', 14), text_color='black', justification='center', pad=((0, 0), (10, 0)))]
]

# Configuração da janela
window = sg.Window('Analisador de Maior e Menor Número', layout, background_color=background_color, finalize=True)

# Lista para armazenar os valores
valores = []

# Loop de eventos
while True:
    event, values = window.read()
    
    if event in (sg.WIN_CLOSED, 'Sair'):
        break
    
    if event == 'Adicionar':
        try:
            valor = int(values['-VALOR-'])
            valores.append(valor)
            window['-LISTA-'].update(valores)
            window['-VALOR-'].update('')
        except ValueError:
            sg.popup_error('Por favor, insira um número inteiro válido.', font=('Arial', 12), background_color=background_color, text_color=text_color)
    
    if event == 'Limpar Lista':
        valores = []
        window['-LISTA-'].update(valores)
    
    if event == 'Calcular':
        maior, menor, cont = calcular_maior_menor(valores)
        if cont > 0:
            resultado = f'Foram informados {cont} valores.\nO maior valor informado foi {maior}.\nO menor valor informado foi {menor}.'
        else:
            resultado = 'Nenhum valor informado.'
        window['-RESULTADO-'].update(resultado)
    
window.close()
