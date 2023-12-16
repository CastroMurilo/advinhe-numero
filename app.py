import tkinter as tk
import random

# Função para verificar o palpite do jogador
def verificar_palpite():
    global tentativas
    palpite = int(palpite_entry.get())
    tentativas += 1
    
    if tentativas > max_tentativas:
        resultado_label.config(text=f"Você esgotou suas {max_tentativas} tentativas. O número era {numero_secreto}.")
        palpite_entry.config(state="disabled")
        verificar_button.config(state="disabled")
    elif palpite < numero_secreto:
        resultado_label.config(text="Tente um número maior.")
    elif palpite > numero_secreto:
        resultado_label.config(text="Tente um número menor.")
    else:
        resultado_label.config(text=f"Parabéns! Você acertou o número em {tentativas} tentativas.")
        palpite_entry.config(state="disabled")
        verificar_button.config(state="disabled")

# Função para reiniciar o jogo
def reiniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    palpite_entry.config(state="normal")
    verificar_button.config(state="normal")
    resultado_label.config(text=f"Tente adivinhar o número entre 1 e 100. Você tem {max_tentativas} tentativas.")

# Inicialização do jogo
numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 10

# Criação da janela principal
janela = tk.Tk()
janela.title("Jogo de Adivinhação")
janela.geometry("300x200")

# Labels
titulo_label = tk.Label(janela, text="Jogo de Adivinhação", font=("Arial", 16))
titulo_label.pack(pady=10)

resultado_label = tk.Label(janela, text=f"Tente adivinhar o número entre 1 e 100. Você tem {max_tentativas} tentativas.", font=("Arial", 12))
resultado_label.pack(pady=10)

# Entrada de palpite
palpite_entry = tk.Entry(janela, width=5)
palpite_entry.pack()

# Botão para verificar o palpite
verificar_button = tk.Button(janela, text="Verificar", command=verificar_palpite)
verificar_button.pack(pady=10)

# Botão para reiniciar o jogo
reiniciar_button = tk.Button(janela, text="Reiniciar Jogo", command=reiniciar_jogo)
reiniciar_button.pack()

janela.mainloop()
