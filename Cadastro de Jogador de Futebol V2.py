import time
import sys

# Função para colorir o texto
def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

# Cores
RED = '31'
GREEN = '32'
YELLOW = '33'

# Função para adicionar pontos enquanto computa os dados
def compute_data():
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    print()

# Dados do jogador
jogador = {}
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}?  ')))

jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

# Computando dados com pontos
print("Computando dados", end="")
compute_data()

print('-=' * 30)
print(jogador)
print('-=' * 30)

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(jogador['gols']):
    if v > 2:
        color = GREEN
    elif v >= 1:
        color = YELLOW
    else:
        color = RED
    print(f'   => Na partida {i}, fez {color_text(v, color)} gols.')

print(f'Foi um total de {jogador["total"]} gols.')

# Mensagem de despedida
print(color_text("Obrigado por utilizar o sistema de acompanhamento de desempenho! Até logo!", GREEN))
