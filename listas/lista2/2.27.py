def main():

    valor = float(input('Informe o valor total da compra:'))
    parcelas = int(input('Informe a quantidade de parcelas:'))
    total, v_parcela = calcula_total(valor, parcelas)
    
    print(f'(PARCELANDO EM {parcelas} VEZES) O valor por parcela fica em R${v_parcela}, totalizando R${total}.')

def calcula_total(valor, parcelas):

    if (parcelas <= 3):
          juros = 0.000
    elif (parcelas <= 7):
          juros = 0.005
    elif (parcelas <= 12):
          juros = 0.015
    elif (parcelas <= 20):
         juros = 0.03 

    total = valor + (valor*juros)
    valor_por_parcela = round(total / parcelas, 2)

    return total, valor_por_parcela
       
main()