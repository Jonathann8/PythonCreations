import PySimpleGUI as sg
import random
import string

# Função para gerar senhas
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + '@#$%&*!'
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Função para gerar nicknames aleatórios
def gerar_nickname():
    adjetivos = ['Speedy', 'Cool', 'Mighty', 'Silent', 'Brave', 'Crazy', 'Wild', 'Smart', 'Funky', 'Chill', 'Swift', 'Bold', 'Lone', 'Fiery', 'Glorious']
    substantivos = ['Lion', 'Wizard', 'Ninja', 'Eagle', 'Panther', 'Shadow', 'Tiger', 'Falcon', 'Wolf', 'Phoenix', 'Dragon', 'Knight', 'Viper', 'Hawk', 'Raven']
    nickname = random.choice(adjetivos) + random.choice(substantivos) + str(random.randint(1, 999))
    return nickname

# Listas para armazenar o histórico de senhas e nicknames
historico_senhas = []
historico_nicknames = []

# Estilo dos botões
button_style = {'button_color': ('white', '#1DB954'), 'font': ('Helvetica', 16), 'border_width': 0, 'pad': (10, 10)}

# Layout da aba de geração de senhas
layout_senhas = [
    [sg.Text('Digite o tamanho da senha:', font=('Helvetica', 16), background_color='#191414', text_color='#1DB954')],
    [sg.InputText(key='tamanho', background_color='#191414', text_color='white', font=('Helvetica', 16), pad=(0, 10))],
    [sg.Button('Gerar Senha', button_color=('white', '#1DB954'), font=('Helvetica', 16), border_width=0, pad=(10, 10))],
    [sg.Text('Senha gerada:', font=('Helvetica', 16), background_color='#191414', text_color='#1DB954')],
    [sg.InputText(key='senha', readonly=True, background_color='#1DB954', text_color='black', font=('Helvetica', 16), pad=(0, 10))],
    [sg.Button('Histórico', button_color=('white', '#1DB954'), font=('Helvetica', 16), border_width=0, pad=(10, 10))]
]

# Layout da aba de geração de nicknames
layout_nicknames = [
    [sg.Button('Gerar Nickname', button_color=('white', '#1DB954'), font=('Helvetica', 16), border_width=0, pad=(10, 10))],
    [sg.Text('Nickname gerado:', font=('Helvetica', 16), background_color='#191414', text_color='#1DB954')],
    [sg.InputText(key='nickname', readonly=True, background_color='#1DB954', text_color='black', font=('Helvetica', 16), pad=(0, 10))],
    [sg.Button('Histórico Nicknames', button_color=('white', '#1DB954'), font=('Helvetica', 16), border_width=0, pad=(10, 10))]
]

# Layout principal com abas
layout = [
    [sg.Text('KeyForge 2.0', font=('Helvetica', 28), background_color='#191414', text_color='#1DB954')],
    [sg.TabGroup([[sg.Tab('Gerar Senhas', layout_senhas, background_color='#191414'),
                   sg.Tab('Gerar Nicknames', layout_nicknames, background_color='#191414')]], background_color='#191414')],
    [sg.Text('KeyForgeV2', font=('Helvetica', 12), background_color='#191414', text_color='#1DB954', justification='center', pad=((0,0),(20,0)))],
    [sg.Button('Sair', button_color=('white', '#E91E63'), font=('Helvetica', 16), border_width=0, pad=(10, 10))]
]

# Janela principal
window = sg.Window('KeyForge 2.0', layout, background_color='#191414', resizable=True)

# Loop principal do programa
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    
    if event == 'Gerar Senha':
        try:
            tamanho = int(values['tamanho'])
            senha = gerar_senha(tamanho)
            window['senha'].update(senha)
            historico_senhas.append(senha)  # Adiciona a senha gerada ao histórico
        except ValueError:
            sg.popup('Por favor, insira um número válido para o tamanho da senha.', background_color='#191414', text_color='white', font=('Helvetica', 16))
    
    if event == 'Gerar Nickname':
        nickname = gerar_nickname()
        window['nickname'].update(nickname)
        historico_nicknames.append(nickname)  # Adiciona o nickname gerado ao histórico
    
    if event == 'Histórico':
        # Exibe o histórico de senhas em uma nova janela
        layout_historico = [
            [sg.Text('Histórico de Senhas:', font=('Helvetica', 16), background_color='#191414', text_color='#1DB954')],
            [sg.Multiline('\n'.join(historico_senhas), size=(40, 10), font=('Helvetica', 14), background_color='#1DB954', text_color='black', disabled=True, key='Multiline')],
            [sg.Button('Apagar Histórico', button_color=('white', '#1DB954'), font=('Helvetica', 16), border_width=0, pad=(10, 10)), sg.Button('Fechar', button_color=('white', '#1DB954'), font=('Helvetica', 16), border_width=0, pad=(10, 10))]
        ]
        
        window_historico = sg.Window('Histórico de Senhas', layout_historico, background_color='#191414')
        
        while True:
            event_hist, _ = window_historico.read()
            if event_hist == sg.WINDOW_CLOSED or event_hist == 'Fechar':
                window_historico.close()
                break
            if event_hist == 'Apagar Histórico':
                historico_senhas.clear()  # Limpa o histórico
                window_historico['Multiline'].update('')  # Limpa o conteúdo da exibição
    
    if event == 'Histórico Nicknames':
        # Exibe o histórico de nicknames em uma nova janela
        layout_historico_nicknames = [
            [sg.Text('Histórico de Nicknames:', font=('Helvetica', 16), background_color='#191414', text_color='#1DB954')],
            [sg.Multiline('\n'.join(historico_nicknames), size=(40, 10), font=('Helvetica', 14), background_color='#1DB954', text_color='black', disabled=True, key='MultilineNicknames')],
            [sg.Button('Apagar Histórico Nicknames', button_color=('white', '#1DB954'), font=('Helvetica', 16), border_width=0, pad=(10, 10)), sg.Button('Fechar', button_color=('white', '#1DB954'), font=('Helvetica', 16), border_width=0, pad=(10, 10))]
        ]
        
        window_historico_nicknames = sg.Window('Histórico de Nicknames', layout_historico_nicknames, background_color='#191414')
        
        while True:
            event_hist_nick, _ = window_historico_nicknames.read()
            if event_hist_nick == sg.WINDOW_CLOSED or event_hist_nick == 'Fechar':
                window_historico_nicknames.close()
                break
            if event_hist_nick == 'Apagar Histórico Nicknames':
                historico_nicknames.clear()  # Limpa o histórico
                window_historico_nicknames['MultilineNicknames'].update('')  # Limpa o conteúdo da exibição

window.close()
