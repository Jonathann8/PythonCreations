import tkinter as tk
from tkinter import messagebox
import time

# Cores que escolhi 
BACKGROUND_COLOR = "#000000"  # Preto
TEXT_COLOR = "#00BFFF"  # Azul claro
#Programa principal:
def compute_data():
    for _ in range(3):
        output_label.config(text=output_label.cget("text") + '.')
        root.update()
        time.sleep(1)

def show_intro():
    output_label.config(text="Bem-vindo ao programa de cálculo de preços de produtos!\n"
                              "Por favor, insira os produtos e seus preços.\n")
    root.update()
    time.sleep(1)

def add_product():
    produto = product_entry.get()
    if produto == "":
        messagebox.showwarning("Entrada inválida", "Por favor, insira o nome do produto.")
        return

    try:
        preço = float(price_entry.get())
    except ValueError:
        messagebox.showwarning("Entrada inválida", "Por favor, insira um preço válido.")
        return

    # Atualiza os valores globais
    global cont, total, totmil, menor, maior, barato, caro

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

    # Exibe produtos adicionados até o momento
    added_products = f"Produto: {produto} | Preço: R${preço:.2f}\n"
    current_output = output_label.cget("text") + added_products
    output_label.config(text=current_output)

    # Reseta as entradas
    product_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

def finalize_purchase():
    if cont == 0:
        messagebox.showwarning("Nenhum Produto", "Nenhum produto foi adicionado!")
        return

    compute_data()

    output = '{:-^40}\n'.format(' FIM DO PROGRAMA ')
    total_color = "green" if total > 1000 else "yellow"
    output += f'O total da compra foi R${total:.2f}\n'
    output += f'Temos {totmil} produtos custando mais de R$1000.00\n'
    output += f'O produto mais barato foi {barato} que custa R${menor:.2f}\n'
    output += f'O produto mais caro foi {caro} que custa R${maior:.2f}\n'
    output += "Obrigado por utilizar o programa! Volte sempre!"

    output_label.config(text=output, fg=total_color)

# Aplicando a interface gráfica
root = tk.Tk()
root.title("App de Compra Simples")
root.geometry("400x400")
root.config(bg=BACKGROUND_COLOR)

# Inicializa as variáveis globais
cont = total = totmil = menor = maior = 0
barato = caro = ''

# Label de introdução e saída
output_label = tk.Label(root, text="", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, justify=tk.LEFT, wraplength=380)
output_label.pack(pady=10)

# Entrada do nome do produto
product_label = tk.Label(root, text="Nome do produto:", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
product_label.pack()
product_entry = tk.Entry(root, width=30)
product_entry.pack()

# Entrada do preço do produto
price_label = tk.Label(root, text="Preço: R$", fg=TEXT_COLOR, bg=BACKGROUND_COLOR)
price_label.pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

# Botão para adicionar o produto
add_button = tk.Button(root, text="Adicionar Produto", command=add_product, bg=TEXT_COLOR, fg=BACKGROUND_COLOR)
add_button.pack(pady=5)

# Botão para finalizar a compra
finalize_button = tk.Button(root, text="Finalizar Compra", command=finalize_purchase, bg=TEXT_COLOR, fg=BACKGROUND_COLOR)
finalize_button.pack(pady=5)

# Executa a introdução
show_intro()

root.mainloop()
