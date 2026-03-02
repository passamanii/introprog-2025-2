def main():
    
    ipi = int(input('Informe a porcentagem de IPI à ser acrescido no valor:'))
    codigo1, valor1, quant1 = pedir_informacoes()
    codigo2, valor2, quant2 = pedir_informacoes()
    preco = calcular_preco(ipi, valor1, quant1, valor2, quant2)
    print(f'O total à ser pago é R${preco}.')

def pedir_informacoes():

    codigo = int(input('Informe o código do produto:'))
    valor = float(input('Informe o valor do produto:'))
    quantidade = int(input('Informe a quantidade de produtos:'))

    return codigo, valor, quantidade

def calcular_preco(ipi, value1, quant1, value2, quant2):

    price = (((value1*quant1)+(value2*quant2))*((ipi/100)+1))
    return price

main()