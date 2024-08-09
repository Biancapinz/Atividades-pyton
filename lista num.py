import math
number= list(range(0, 21, 2))

soma= sum(number)
soma = math.fsum(number)


print("Números pares:", number)
print("Sua some é:", soma)