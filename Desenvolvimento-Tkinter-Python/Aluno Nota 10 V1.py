import tkinter as tk
from tkinter import messagebox

def calcular_situacao():
    try:
        nome = entry_nome.get()
        media = float(entry_media.get())
    except ValueError:
        messagebox.showerror("Entrada inválida", "Por favor, insira valores válidos.")
        return

    resultado['Nome'] = nome
    resultado['Média'] = media

    if media >= 7:
        resultado['Situação'] = "Aprovado"
        label_situacao.config(fg='green')
    elif 5 <= media < 7:
        resultado['Situação'] = "Recuperação"
        label_situacao.config(fg='orange')
    else:
        resultado['Situação'] = "Reprovado"
        label_situacao.config(fg='red')

    label_nome_valor.config(text=resultado['Nome'])
    label_media_valor.config(text=f"{resultado['Média']:.2f}")
    label_situacao_valor.config(text=resultado['Situação'])

# Configuração da janela principal
root = tk.Tk()
root.title("Sistema de Notas do Colégio")
root.geometry("400x300")

# Widgets de entrada
tk.Label(root, text="Nome do Aluno:").pack()
entry_nome = tk.Entry(root)
entry_nome.pack()

tk.Label(root, text="Média do Aluno:").pack()
entry_media = tk.Entry(root)
entry_media.pack()

# Botão para calcular a situação
tk.Button(root, text="Calcular Situação", command=calcular_situacao).pack()

# Labels para exibir o resultado
tk.Label(root, text="Relatório do Aluno", font=('Helvetica', 14, 'bold')).pack(pady=10)

frame_resultado = tk.Frame(root)
frame_resultado.pack()

label_nome = tk.Label(frame_resultado, text="Nome:", font=('Helvetica', 12))
label_nome.grid(row=0, column=0, sticky='w')
label_nome_valor = tk.Label(frame_resultado, text="", font=('Helvetica', 12))
label_nome_valor.grid(row=0, column=1, sticky='w')

label_media = tk.Label(frame_resultado, text="Média:", font=('Helvetica', 12))
label_media.grid(row=1, column=0, sticky='w')
label_media_valor = tk.Label(frame_resultado, text="", font=('Helvetica', 12))
label_media_valor.grid(row=1, column=1, sticky='w')

label_situacao = tk.Label(frame_resultado, text="Situação:", font=('Helvetica', 12))
label_situacao.grid(row=2, column=0, sticky='w')
label_situacao_valor = tk.Label(frame_resultado, text="", font=('Helvetica', 12))
label_situacao_valor.grid(row=2, column=1, sticky='w')

# Dicionário para armazenar os resultados
resultado = {}

# Iniciar a interface
root.mainloop()
