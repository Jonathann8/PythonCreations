import PySimpleGUI as sg
import random
import string

# Leia-me: Manual do Programa
"""
Nome: KeyForge
Versão: KeyForgeV1

Descrição:
KeyForge é um gerador de senhas aleatórias que permite ao usuário gerar senhas seguras com uma combinação de letras maiúsculas, minúsculas, números e caracteres especiais.
A aplicação oferece também um histórico das senhas geradas, com a opção de limpar esse histórico.

Como usar:
1. Digite o tamanho desejado da senha no campo de entrada.
2. Clique no botão 'Random' para gerar uma nova senha.
3. A senha gerada será exibida no campo abaixo.
4. Para ver o histórico de senhas geradas, clique no botão 'Histórico'.
5. Dentro da janela de histórico, você pode apagar todas as senhas clicando em 'Apagar Histórico'.
6. Para sair do programa, clique no botão 'Sair'.


"""

# Função para gerar a senha
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + '@#$%&*!'
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Lista para armazenar o histórico de senhas
historico_senhas = []

# Layout da interface
sg.theme_background_color('#000000')  # Cor preta para a interface
layout = [
    [sg.Text('KeyForge', font=('Helvetica', 28), background_color='#000000', text_color='white')],
    [sg.Text('Digite o tamanho da senha:', font=('Helvetica', 16), background_color='#000000', text_color='white')],
    [sg.InputText(key='tamanho', background_color='#333333', text_color='white', font=('Helvetica', 16))],
    [sg.Button('Random', button_color=('white', '#333333'), font=('Helvetica', 16)), 
     sg.Button('Histórico', button_color=('white', '#333333'), font=('Helvetica', 16)), 
     sg.Button('Sair', button_color=('white', '#333333'), font=('Helvetica', 16))],
    [sg.Text('Senha gerada:', font=('Helvetica', 16), background_color='#000000', text_color='white')],
    [sg.InputText(key='senha', readonly=True, background_color='#ffffff', text_color='black', font=('Helvetica', 16))],
    [sg.Text('KeyForgeV1', font=('Helvetica', 12), background_color='#000000', text_color='white', justification='center', pad=((0,0),(20,0)))],
]

# Janela principal
window = sg.Window('KeyForge', layout)

# Loop principal do programa
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    
    if event == 'Random':
        try:
            tamanho = int(values['tamanho'])
            senha = gerar_senha(tamanho)
            window['senha'].update(senha)
            historico_senhas.append(senha)  # Adiciona a senha gerada ao histórico
        except ValueError:
            sg.popup('Por favor, insira um número válido para o tamanho da senha.', background_color='#333333', text_color='white', font=('Helvetica', 16))
    
    if event == 'Histórico':
        # Exibe o histórico em uma nova janela
        layout_historico = [
            [sg.Text('Histórico de Senhas:', font=('Helvetica', 16), background_color='#000000', text_color='white')],
            [sg.Multiline('\n'.join(historico_senhas), size=(40, 10), font=('Helvetica', 14), background_color='#ffffff', text_color='black', disabled=True, key='Multiline')],
            [sg.Button('Apagar Histórico', button_color=('white', '#333333'), font=('Helvetica', 16)), sg.Button('Fechar', button_color=('white', '#333333'), font=('Helvetica', 16))]
        ]
        
        window_historico = sg.Window('Histórico de Senhas', layout_historico)
        
        while True:
            event_hist, _ = window_historico.read()
            if event_hist == sg.WINDOW_CLOSED or event_hist == 'Fechar':
                window_historico.close()
                break
            if event_hist == 'Apagar Histórico':
                historico_senhas.clear()  # Limpa o histórico
                window_historico['Multiline'].update('')  # Limpa o conteúdo da exibição

window.close()

