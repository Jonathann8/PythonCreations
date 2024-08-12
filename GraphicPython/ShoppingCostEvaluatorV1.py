import PySimpleGUI as sg

def compute_data():
    for _ in range(3):
        sg.popup_animated(sg.DEFAULT_BASE64_LOADING_GIF, no_titlebar=True, keep_on_top=True)
        sg.time.sleep(1)
    sg.popup_animated(None)

def show_intro():
    sg.popup("Bem-vindo ao programa de cálculo de preços de produtos!", 
             "Por favor, insira os produtos e seus preços.")

def process_products():
    total = totmil = menor = maior = 0
    barato = caro = ''
    cont = 0

    while True:
        produto = sg.popup_get_text('Nome do produto:')
        if produto is None:
            break
        while True:
            try:
                preço = float(sg.popup_get_text('Preço: R$'))
                break
            except ValueError:
                sg.popup_error("Por favor, insira um preço válido.")
        
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

        resp = sg.popup_yes_no('Quer continuar?', default_button='Sim')
        if resp == 'No':
            break

    return total, totmil, menor, barato, maior, caro

# Exibir introdução
show_intro()

# Processar produtos
total, totmil, menor, barato, maior, caro = process_products()

# Exibir processamento de valores
compute_data()

# Exibir resultados
sg.popup("FIM DO PROGRAMA", 
         f'O total da compra foi R${total:10.2f}',
         f'Temos {totmil} produtos custando mais de R$1000.00',
         f'O produto mais barato foi {barato} que custa R${menor:.2f}',
         f'O produto mais caro foi {caro} que custa R${maior:.2f}')

sg.popup("Obrigado por utilizar o programa! Volte sempre!")
