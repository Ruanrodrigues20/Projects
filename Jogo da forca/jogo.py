from palavra import palavra
from random import choice
import time


def assunto():
    # recolhe do jogador tema da palavra
    while True:
        d = input('Qual o assunto [fruta/profissoes/animais/cores/objetos/paises]? ').lower()
        if d[0] == 'f':
            return 'frutas'
        elif d[:3] == 'pro':
            return 'profissoes'
        elif d[0] == 'a':
            return 'animais'
        elif d[0] == 'c':
            return 'cores'
        elif d[0] == 'o':
           return 'objetos'
        elif d[:3] == 'pai':
            return 'paises'



def nivel():
    # recolhe do jogador nível de dificuldade
    print('Muito bem, agora vamos para o nível: ')
    while True:
        nivel = input('Qual o nível de dificuldade [facil/medio/dificil]? ').lower()
        if nivel[0] == 'f':
            return 'facil'
        elif nivel[0] == 'm':
            return 'medio'
        elif nivel[0] == 'd':
            return 'dificil'


def dificuldade():
    # Retorna a palavra acerca do tema e nivel escolhido

    tema = assunto()
    n = nivel()
    palavra_escolhida = palavra(tema, n)

    return palavra_escolhida


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
    print('Jogo da forca'.center(60))
    print(' ')
    a = '-'
    print(f'Considere {a} como um espaço.')
    print(' ')
    continuar = 's'
    while continuar == 's':
        forca()
        cont = input('Mais uma rodada [s/n]? ').lower()
        continuar = cont[0]
        print(' ')

    print('Até a próxima!')
    time.sleep(2)


main()