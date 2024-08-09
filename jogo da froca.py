import randon

def escolher_palavra():
    palavras = ['Bianca', 'Giulia', 'Rafa','Camile']
    return random.choice(palavras).upper()

def jogo_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = []
    tentativas = 6

    print("bem vindo ao joguinho da adivinhação!!")
    print("_ "* len(palavra))

    while tentativas > 0:
        tentativa = input('Digite uma letra:').upper()


        if tentativa in letras_adivinhadas:
            print('Você já tentou essa letra. tente outra')
            continue


        letras_adivinhadas.append(tentativas)

        if tentativa in palavra:
            print('Boa! a  letra está na palavra')

        else:
            tentativas -= 1
            print('Errado. você tem {} tentativas restantes.'.format(tentativas))

        Palavra_oculta = "".join([letra if letra in letras_adivinhadas else '_' for letra in palavra])
        print(''.join(palavra_oculta))

    if '_' not in palavra_oculta:
        print('Você perdeu!! a apalavra era {}'.format(palavra))

jogo_forca()