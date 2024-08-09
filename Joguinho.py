import random


def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    print("OIEEEE, este é o jogo da bibi de adivinhação")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar qual é!")

    while not acertou:
        palpite = int(input("Digite seu chute: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("chuta mais alto")
        elif palpite > numero_secreto:
            print("chuta mais baixo")
        else:
            acertou = True
            print(f"Boaaaaa você consegiu em  {tentativas} tentativas.")


jogo_adivinhacao()
