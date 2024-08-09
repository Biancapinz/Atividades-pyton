numeros = []

for i in range(2):
    numero = int(input(f'Digite o {i+1}º número: '))
    numeros.append(numero)
    resultado = sum(numeros)
    print(resultado)
