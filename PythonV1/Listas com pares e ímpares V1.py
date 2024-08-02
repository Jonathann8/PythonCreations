import sys
import time


def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"


BLUE = '34'
YELLOW = '33'


def compute_data():
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    print()


def show_intro():
    print("Bem-vindo ao programa de identificação de valores pares e ímpares!")
    print("Por favor, insira 7 valores para começar.")
    time.sleep(1)


def process_values():
    nums = [[], []]
    for c in range(1, 8):
        while True:
            try:
                value = int(input(f'Digite o {c}º valor: '))
                break
            except ValueError:
                print(color_text("Por favor, insira um número válido.", YELLOW))
        if value % 2 == 0:
            nums[0].append(value)
        else:
            nums[1].append(value)
    return nums


show_intro()


nums = process_values()


print("Processando valores", end="")
compute_data()


nums[0].sort()
nums[1].sort()


print('-=' * 30)
print(f'Os valores pares digitados foram: {color_text(nums[0], BLUE)}')
print(f'Os valores ímpares digitados foram: {color_text(nums[1], YELLOW)}')
print('-=' * 30)


print(color_text("Obrigado por utilizar o programa! Tenha um ótimo dia!", BLUE))
