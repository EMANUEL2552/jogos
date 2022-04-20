print('*********************************')
print('***Bem vindo ao jogo da Forca!***')
print('*********************************')

palavra_secreta = 'banana'
letras_acertadas = ['_', '_', '_', '_', '_', '_']
acertou = False
enforcou = False
erros = 0
print(letras_acertadas)
while (not enforcou and not acertou):
    chute = input('qual a letra ?')
    if (chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[posicao] = letra
            posicao = posicao + 1

        else:
            erros += 1

        enforcou = erros == 6

        if(chute == letra):
          letras_acertadas[posicao] = letra
        posicao += 1
        print('encontrei a letra {} na posiçao {}'.format(letra, posicao))
        print(letras_acertadas)
        posicao = posicao + 1
    print('jogando....')

print('fim do jogo')