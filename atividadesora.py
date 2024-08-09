import math

def resolver_equacao_segundo_grau(a,b,c):

    discriminante = b**2 - 4*a*c

    if discriminante > 0:

        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return 'Duas soluções reais : x1 = {}, x2 = {}'.format(x1,x2)
    elif discriminante == 0:
        x = - b / (2*a)
        return "uma solução real: x = {}".format(x)
    else:
        return 'nenhuma solução real'

a = float(input('Digite o coeficiente a (Diferente de 0): '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

if a == 0:
    print('O coeficiente a deve ser diferente de zero para uma equção de primeiro grau.')
else:
    resultado = resolver_equacao_segundo_grau(a,b,c)
    print(resultado)