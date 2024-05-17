from palavra import palavra
from random import choice
import time

def dificuldade():
    # verifica qual o nível de dificuldade da palavra que o jogador escolheu e
    # retorna uma string adequada ao nivel escolhido
    
    para = False
    while not para:
        d = input('Qual o assunto [fruta/profissoes/animais/cores/objetos/paises]? ').lower()
        if d[0] == 'f':
            assunto = 'frutas'
            para = True
        elif d[:3] == 'pro':
            assunto = 'profissoes'
            para = True
        elif d[0] == 'a':
            assunto = 'animais'
            para = True
        elif d[0] == 'c':
            assunto ='cores'
        elif d[0] == 'o':
            assunto = 'objetos'
        elif d[:3] == 'pai':
            assunto = 'paises'
    
    para = False
    print('Muito bem, agora vamos para o nível')
    while not para:
        nivel = input('Qual o nível de dificuldade [facil/medio/dificil]? ')
        if nivel[0] == 'f':
            str_escolhida = palavra(assunto, nivel)
        elif nivel[0] == 'm':
            str_escolhida = palavra(assunto, nivel)
        elif nivel[0] == 'd':
            str_escolhida = palavra(assunto, nivel)


    return str_escolhida


def forca():
    # jogo da forco propriamente
    palavra = dificuldade()

    car = [i for i in palavra]
    tentativas = 6
    acertos = 0
    saida = ['_' for i in range(len(car))]
    letras = []

    while acertos < len(car) and tentativas > 0:
        entrada_0 = input('Diga letra/palavra: ').lower()

        # Verifica se o usuário adivinhou a palavra inteira
        if len(entrada_0) > 1:
            if list(entrada_0) == car:
                saida = car
                acertos = len(car)
                break
            else:
                tentativas -= 1
                print('Errou!')
        
        # Verifica se o usuário adivinhou uma letra
        else:
            letra = entrada_0[0]
            if letra in letras:
                print('Você já tentou essa letra.')
            else:
                letras.append(letra)
                if letra in car:
                    for j in range(len(car)):
                        if letra == car[j]:
                            saida[j] = car[j]
                            acertos += 1
                else:
                    tentativas -= 1
                    print('Errou!')
        
        print('')
        print(' '.join(saida))
        print(f'Você tem {acertos} acertos e {tentativas} tentativas')
        print('')

    if acertos == len(car):
        print('PARABÉNS, você conseguiu!')
    else:
        print('TENTE DA PRÓXIMA VEZ')
        print(f'A palavra era {palavra}')
    print(' ')


def main():
    print('Jogo da forca')
    continuar = 's'
    while continuar == 's':
        forca()
        cont = input('Mais uma rodada [s/n]? ').lower()
        continuar = cont[0]
        print(' ')

    print('Até a próxima!')
    time.sleep(3)


main()