# Função para converter BRL para USD
def conv(brl, taxa):
    usd = brl * taxa
    return usd

brl = float(input("Digite o valor em Reais: "))
taxa = 0.20
usd = conv(brl, taxa)

print(f"{brl} reais é equivalente a {usd} dolareszinhos")
