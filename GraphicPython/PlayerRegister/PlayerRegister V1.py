import PySimpleGUI as sg

time = list()
jogador = {}
partidas = list()

layout = [
    [sg.Text('Nome do Jogador:'), sg.Input(key='nome')],
    [sg.Text('Quantas partidas jogou?'), sg.Input(key='partidas')],
    [sg.Button('Ok'), sg.Button('Sair')],
    [sg.Text('Resultados:'), sg.Multiline(size=(50, 10), key='resultados', disabled=True)]
]

window = sg.Window('Cadastro de Jogadores', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    
    if event == 'Ok':
        jogador.clear()
        jogador['nome'] = values['nome']
        tot = int(values['partidas'])
        partidas.clear()
        for c in range(tot):
            gol = sg.popup_get_text(f'Quantos gols na partida {c + 1}?', 'Gols')
            partidas.append(int(gol))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
        time.append(jogador.copy())

        # Exibir os resultados no campo de texto
        resultados_texto = 'cod  nome           gols               total\n'
        resultados_texto += '-' * 50 + '\n'
        for i, jogador in enumerate(time):
            resultados_texto += f"{i:>3}  {jogador['nome']:<15} {str(jogador['gols']):<18} {jogador['total']}\n"
        
        window['resultados'].update(resultados_texto)
        sg.popup(f"Jogador {jogador['nome']} registrado com sucesso!")

window.close()
