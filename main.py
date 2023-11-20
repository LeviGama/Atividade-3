import tkinter as tk
from tkinter import ttk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        resultado.set(f"O IMC do paciente é: {imc:.2f}")

    except ValueError:
        resultado.set("Por favor, insira valores válidos para peso e altura.")

def resetar():
    entry_nome.delete(0, "end")
    entry_endereco.delete(0, "end")
    entry_peso.delete(0, "end")
    entry_altura.delete(0, "end")
    resultado.set ("")


# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Variáveis de controle
resultado = tk.StringVar()
interpretacao = tk.StringVar()

# Criar widgets
label_nome = ttk.Label(janela, text="Nome do Paciente:")
entry_nome = ttk.Entry(janela)

label_endereco = ttk.Label(janela, text="Endereço Completo:")
entry_endereco = ttk.Entry(janela)

label_peso = ttk.Label(janela, text="Peso em Quilogramas (00.00):")
entry_peso = ttk.Entry(janela)

label_altura = ttk.Label(janela, text="Altura em Metros (0.00):")
entry_altura = ttk.Entry(janela)

botao_calcular = ttk.Button(janela, text="Calcular IMC", command=calcular_imc)

botao_resetar = ttk.Button(janela, text="Resetar", command=resetar)

label_resultado = ttk.Label(janela, textvariable=resultado)


# Layout dos widgets

label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_nome.grid(row=0, column=1, padx=10, pady=5)

label_endereco.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_endereco.grid(row=1, column=1, padx=10, pady=5)

label_peso.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_peso.grid(row=2, column=1, padx=10, pady=5)

label_altura.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_altura.grid(row=3, column=1, padx=10, pady=5)

botao_calcular.grid(row=5, column=0, pady=10)

botao_resetar.grid(row=5, column=1, pady=10)

label_resultado.grid(row=7, column=0, columnspan=2, pady=5)


# Iniciar o loop da interface gráfica
janela.mainloop()