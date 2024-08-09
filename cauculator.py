def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Deu zero:("


num1 = float(input("Olá seja bem vindo a bia cauculadora, digite seu primeiro número: "))
num2 = float(input("Agora seu segundo número: "))

print("Escolha a operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite a opção escolhida (1/2/3/4): ")

if opcao == '1':
    print("Resultado:", adicao(num1, num2))
elif opcao == '2':
    print("Resultado:", subtracao(num1, num2))
elif opcao == '3':
    print("Resultado:", multiplicacao(num1, num2))
elif opcao == '4':
    print("Resultado:", divisao(num1, num2))
else:
    print("Sua opção é invalida!")