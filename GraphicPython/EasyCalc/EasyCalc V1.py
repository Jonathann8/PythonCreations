import tkinter as tk
from tkinter import messagebox

def calculo():
    try:
        n1 = int(entry1.get())
        n2 = int(entry2.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira números válidos.")
        return

    opção = var.get()

    if opção == 1:
        result = n1 + n2
        messagebox.showinfo("Resultado", f'A soma entre {n1} + {n2} é {result}')
    elif opção == 2:
        result = n1 * n2
        messagebox.showinfo("Resultado", f'O resultado de {n1} x {n2} é {result}')
    elif opção == 3:
        if n1 > n2:
            result = n1
        else:
            result = n2
        messagebox.showinfo("Resultado", f'Entre {n1} e {n2} o maior valor é {result}')
    elif opção == 4:
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        var.set(0)
    else:
        messagebox.showerror("Opção inválida", "Tente novamente!")

def sair():
    root.quit()

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Simples")

# Widgets de entrada
tk.Label(root, text="Primeiro valor:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Segundo valor:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Variável para armazenar a opção selecionada
var = tk.IntVar()

# Opções de operação
tk.Radiobutton(root, text="Somar", variable=var, value=1).pack(anchor=tk.W)
tk.Radiobutton(root, text="Multiplicar", variable=var, value=2).pack(anchor=tk.W)
tk.Radiobutton(root, text="Maior", variable=var, value=3).pack(anchor=tk.W)
tk.Radiobutton(root, text="Novos Números", variable=var, value=4).pack(anchor=tk.W)

# Botão para calcular
tk.Button(root, text="Calcular", command=calculo).pack()

# Botão para sair
tk.Button(root, text="Sair", command=sair).pack()

# Iniciar a rface
root.mainloop()

