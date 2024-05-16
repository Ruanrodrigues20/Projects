import tkinter as tk
from tkinter import messagebox

# Configuração inicial do jogo
palavra = 'RUAN'
car = [i for i in palavra]
tentativas = 6
acertos = 0
saida = ['_' for _ in car]
letras = []

# Função para atualizar a interface
def atualizar_interface():
    global acertos, tentativas
    label_saida.config(text=' '.join(saida))
    label_tentativas.config(text=f'Tentativas restantes: {tentativas}')
    label_acertos.config(text=f'Acertos: {acertos}')
    if acertos == len(car):
        messagebox.showinfo("Jogo da Forca", "PARABÉNS, você conseguiu!")
        root.quit()
    elif tentativas <= 0:
        messagebox.showinfo("Jogo da Forca", "TENTE DA PRÓXIMA VEZ")
        root.quit()

# Função para processar a entrada do jogador
def verificar():
    global acertos, tentativas
    entrada = entry.get().upper()
    entry.delete(0, tk.END)
    
    if len(entrada) == 1:  # O jogador entrou com uma única letra
        letra = entrada
        if letra in letras:
            messagebox.showwarning("Aviso", "Você já tentou essa letra.")
        elif letra in car:
            letras.append(letra)
            for i in range(len(car)):
                if car[i] == letra:
                    saida[i] = letra
                    acertos += 1
            messagebox.showinfo("Jogo da Forca", "Acertou!")
        else:
            letras.append(letra)
            tentativas -= 1
            messagebox.showinfo("Jogo da Forca", "Errou!")
    elif entrada == palavra:  # O jogador entrou com a palavra inteira correta
        acertos = len(car)
        saida[:] = car
        atualizar_interface()
    else:  # O jogador entrou com a palavra inteira errada
        tentativas -= 1
        messagebox.showinfo("Jogo da Forca", "Errou a palavra!")

    atualizar_interface()

# Criação da janela principal
root = tk.Tk()
root.title("Jogo da Forca")

# Criação dos widgets
label_instrucoes = tk.Label(root, text="Diga letra/palavra:")
label_instrucoes.pack()

entry = tk.Entry(root)
entry.pack()

button_verificar = tk.Button(root, text="Verificar", command=verificar)
button_verificar.pack()

label_saida = tk.Label(root, text=' '.join(saida), font=("Helvetica", 24))
label_saida.pack()

label_tentativas = tk.Label(root, text=f'Tentativas restantes: {tentativas}')
label_tentativas.pack()

label_acertos = tk.Label(root, text=f'Acertos: {acertos}')
label_acertos.pack()

# Atualização inicial da interface
atualizar_interface()

# Execução da aplicação
root.mainloop()
