import random
palavra_secreta = ''
letras_acertadas = []


def definir_palavra_palavra_secreta():
    global palavra_secreta, letras_acertadas
    arquivo = open('palavras.txt', 'r')

    palavras = [palavra.strip() for palavra in arquivo.readlines()]

    arquivo.close()

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()

    letras_acertadas = ['_' for x in palavra_secreta]

def jogar():
    acabou = False
    tentativas = 6
    while acabou == False:
        global letras_acertadas
        print(letras_acertadas)
        chute = input('Digite uma letra: ').upper().strip()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = chute
                index += 1
        else:
            tentativas -= 1

        if not '_' in letras_acertadas:
            print('Você ganhou')
            acabou = True
        elif tentativas == 0:
            print('Você perdeu')
            acabou = False
