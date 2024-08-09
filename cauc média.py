def calcular_media():
    numeros = []
    print("Digite cinco números:")

    while len(numeros) < 5:
        entrada = input(f"Número {len(numeros) + 1}: ")
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número válido.")

    soma = sum(numeros)
    media = soma / len(numeros)
    return media

# Executando a função
media = calcular_media()
print(f"A média dos números é: {media}")
