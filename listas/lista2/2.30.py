def main():

    cpf, dependentes, renda = pede_informacoes()
    total_imposto = calcula_imposto(dependentes, renda)
    
    print(f'O total de imposto à ser pago é: R${total_imposto}.')

def pede_informacoes():

    cadastro_de_pessoa_fisica = int(input('Informe o CPF (somente números):'))
    dependentes_da_pessoa = int(input('Informe a quantidade de dependentes:'))
    renda_da_pessoa = float(input('Insira a renda mensal aqui:'))

    return cadastro_de_pessoa_fisica, dependentes_da_pessoa, renda_da_pessoa

def calcula_imposto(dependentes, renda):
    
    desconto_dependente = dependentes * (renda*0.05)

    if (renda < 2000):
        desconto = 0
    elif (renda < 3000):
        desconto = (renda*0.05)
    elif (renda < 5000):
        desconto = (renda*0.1)
    elif (renda < 7):
        desconto = (renda*0.15)
    else:
        desconto = (renda*0.2)

    a_pagar = desconto + desconto_dependente

    return a_pagar

main()