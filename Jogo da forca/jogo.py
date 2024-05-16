palavra = 'RUAN'
car = [i for i in palavra]
tentativas = 6
acertos = 0
saida = ['_' for i in range(len(car))]
letras = []

while acertos < len(car) or tentativas > 0:
    if acertos >= len(car): break
    ver = acertos
    entrada_0 = [i for i in input('Diga letra/palavra: ').upper()]
   
    if len(entrada_0) <= len(car):
        for i in range(len(entrada_0)):
            for j in range(len(car)):
                if entrada_0[i] == car[j]:
                    if j > 0:
                        saida[j] = car[j].lower()
                    elif j == 0:
                        saida[j] = car[j]
                
            if not entrada_0[i] in letras and entrada_0[i] in car:
                acertos += 1
            letras.append(entrada_0[i])

    if ver >= acertos:
        tentativas -= 1
        print('Errou!')
        
    print('')
    print(saida)
    print(f'Você tem {acertos} acertos e {tentativas} tentativas')
    print('')


if acertos == len(car):
    print('PARABENS, você conseguiu')
else:
    print('TENTE DA PRÓXIMA VEZ')
    


    