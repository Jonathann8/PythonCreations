import time
import sys

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

GREEN = '32'
YELLOW = '33'

def compute_data():
    for _ in range(3):
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)
    print()

def show_intro():
    print("Bem-vindo ao programa de cálculo de preços de produtos!")
    print("Por favor, insira os produtos e seus preços.")
    time.sleep(1)

def process_products():
    total = totmil = menor = maior = cont = 0
    barato = caro = ''
    while True:
        produto = str(input('Nome do produto: '))
        while True:
            try:
                preço = float(input('Preço: R$'))
                break
            except ValueError:
                print(color_text("Por favor, insira um preço válido.", YELLOW))

        cont += 1
        total += preço
        if preço > 1000:
            totmil += 1
        if cont == 1 or preço < menor:
            menor = preço
            barato = produto
        if cont == 1 or preço > maior:
            maior = preço
            caro = produto

        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp == 'N':
            break

    return total, totmil, menor, barato, maior, caro

show_intro()

total, totmil, menor, barato, maior, caro = process_products()

print("Processando valores", end="")
compute_data()

print('{:-^40}'.format(' FIM DO PROGRAMA '))
total_color = GREEN if total > 1000 else YELLOW
print(f'O total da compra foi {color_text(f"R${total:10.2f}", total_color)}')
print(f'Temos {color_text(totmil, GREEN)} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {color_text(barato, YELLOW)} que custa {color_text(f"R${menor:.2f}", YELLOW)}')
print(f'O produto mais caro foi {color_text(caro, GREEN)} que custa {color_text(f"R${maior:.2f}", GREEN)}')

print(color_text("Obrigado por utilizar o programa! Volte sempre!", GREEN))
