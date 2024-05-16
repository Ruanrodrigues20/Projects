import tkinter as tk

def on_button_click():
    label.config(text="Está pronto?")

palavra = 'RUAN'
car = [i for i in palavra]
tentativas = 6
acertos = 0
saida = ['_' for i in range(len(car))]
letras = []

# Criação da janela principal
root = tk.Tk()
root.title("Jogo da Forca")
root.geometry("300x200")

# Criação de um rótulo (label)
label = tk.Label(root, text="Clique no botão")
label.pack(pady=20)

# Criação de um botão
button = tk.Button(root, text="Clique-me", command=on_button_click)
button.pack(pady=10)

# Execução da aplicação
root.mainloop()
