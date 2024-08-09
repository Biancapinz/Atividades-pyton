def p(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

num = int(input("Digite um número: "))
if p(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
