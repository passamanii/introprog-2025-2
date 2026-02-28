def main():

    valor_vendas = float(input('Informe o valor das vendas brutas da semana passada:'))
    sal_semana = calcula_salario_semana(valor_vendas)
    print(f'O valor à ser recebido pelo vendedor é de R${(sal_semana):.2f}.')
    
def calcula_salario_semana(valor):
    
    wage = 200
    wage += (valor*0.09)

    if (valor > 1000):
        wage += 800
    
    return wage

main()