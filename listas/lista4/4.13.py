def main():

    gallon = float(input('Informe o preço do galão:'))
    rate = float(input('Informe a taxa de conversão Dólar-Real:'))
    liter = CONVERTE_PRECOS(gallon, rate)

    print(f'Se adotássemos a precificação estadunidense no Brasil, o litro da gasolina estaria por volta de R${(liter):.2f}.')

def CONVERTE_PRECOS(g, r):

    price_per_liter = (g/3.7854)
    price_to_real = (price_per_liter*r)

    return price_to_real

main()