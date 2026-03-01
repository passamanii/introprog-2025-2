def main():
     
    consumo_anterior = float(input('Informe o consumo de energia do mês anterior:'))
    consumo_atual = float(input('Informe o consumo de energia do mês atual:'))

    consumo_res = consumo_atual - consumo_anterior

    if (consumo_res <= 70):
        tarifa = 0.09
    elif (consumo_res <= 150):
        tarifa = 0.20
    elif (consumo_res <= 200):
        tarifa = 0.23
    else:
        tarifa = 0.26

    conta_energia = consumo_res * tarifa

    print(f'A conta de energia do mês atual ficou R${(conta_energia):.2f}.')

main()