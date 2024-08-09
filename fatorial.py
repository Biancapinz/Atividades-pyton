def fatorial(n):

    if n < 0:
        raise ValueError("O número deve ser não-negativo.")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

try:
    numero = int(input("Digite um número inteiro não-negativo para calcular o fatorial: "))
    print(f"O fatorial de {numero} é {fatorial(numero)}.")
except ValueError as e:
    print(f"Erro: {e}. Certifique-se de digitar um número inteiro não-negativo.")
