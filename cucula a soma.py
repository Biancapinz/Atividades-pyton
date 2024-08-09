
quantidade = int(input("Quantos números você deseja somar? "))
numeros = []
for _ in range(quantidade):
    numero = float(input("Digite um número: "))
    numeros.append(numero)
soma = 0
for numero in numeros:
    soma += numero
print(f"A soma de todos é: {soma}")

