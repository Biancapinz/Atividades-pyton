def count_vogais(string):
    vogais = "aeiou"
    contador = 0


    for char in string:

        if char in vogais:
            contador += 1

    return contador

texto = input("Digite uma palavra ou frase: ")

numbervogais = count_vogais(texto)

print(f"O número de vogais na string é: {numbervogais}")
