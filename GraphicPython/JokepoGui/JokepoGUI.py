import PySimpleGUI as sg
from random import randint
from time import sleep

# Função para determinar o resultado do jogo
def determinar_resultado(jogador, computador):
    itens = ('Pedra', 'Papel', 'Tesoura')
    if computador == jogador:
        return 'EMPATE'
    elif (computador == 0 and jogador == 1) or (computador == 1 and jogador == 2) or (computador == 2 and jogador == 0):
        return 'O JOGADOR VENCEU'
    else:
        return 'O COMPUTADOR VENCEU'

# Layout da interface gráfica com escala maior
layout = [
    [sg.Text('Escolha sua jogada:', font=('Helvetica', 16))],
    [sg.Button('Pedra', font=('Helvetica', 14)), sg.Button('Papel', font=('Helvetica', 14)), sg.Button('Tesoura', font=('Helvetica', 14))],
    [sg.Text('', size=(30, 5), key='resultado', font=('Helvetica', 14))],
    [sg.Button('Sair', font=('Helvetica', 14))]
]

# Criar a janela
window = sg.Window('Jokepo Game', layout, resizable=True, finalize=True)

while True:
    event, _ = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if event in ['Pedra', 'Papel', 'Tesoura']:
        jogador = ['Pedra', 'Papel', 'Tesoura'].index(event)
        computador = randint(0, 2)
        resultados = ['Pedra', 'Papel', 'Tesoura']
        resultado_jogo = determinar_resultado(jogador, computador)
        
        # Atualizar o texto de resultado
        resultado_texto = f'Computador jogou: {resultados[computador]}\n'
        resultado_texto += f'Jogador jogou: {resultados[jogador]}\n'
        resultado_texto += f'Verdicto: {resultado_jogo}\n'
        
        # Mostrar quem venceu
        if resultado_jogo == 'O JOGADOR VENCEU':
            resultado_texto += 'Parabéns! Você venceu!'
        elif resultado_jogo == 'O COMPUTADOR VENCEU':
            resultado_texto += 'VOCÊ PERDEU. Tente novamente!'
        else:
            resultado_texto += 'Foi um empate. Jogue novamente!'
        
        window['resultado'].update(resultado_texto)
        
        # Pequena pausa para efeito de animação
        sg.popup('JO\nKEN\nPÔ!!!', no_titlebar=True, keep_on_top=True, font=('Helvetica', 16))
        sleep(1)

window.close()
