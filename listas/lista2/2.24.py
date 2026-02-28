def main():

    val_compra = float(input('Informe o valor total da compra:'))
    parcelas = verifica_parcelas(val_compra)
    calcula_parcelas(val_compra, parcelas)
    
def verifica_parcelas(valor):
    
    if (valor <= 500):
        quantidade_parcelas = 5
    else:
        quantidade_parcelas = 8

    return quantidade_parcelas

def calcula_parcelas(valor, parcelas):

    if (parcelas == 5):
        p2x = round(valor/2, 2)
        p3x = round(valor/3, 2)
        p4x = round(valor/4, 2)
        p5x = round(valor/5, 2)
        print(f'2X SEM JUROS: R${p2x}\n3X SEM JUROS: R${p3x}\n4X SEM JUROS: R${p4x}\n5X SEM JUROS: R${p5x}')
    elif (parcelas == 8):
        p2x = round(valor/2, 2)
        p3x = round(valor/3, 2)
        p4x = round(valor/4, 2)
        p5x = round(valor/5, 2)
        p6x = round(valor/6, 2)
        p7x = round(valor/7, 2)
        p8x = round(valor/8, 2)
        print(f'2X SEM JUROS: R${p2x}\n3X SEM JUROS: R${p3x}\n4X SEM JUROS: R${p4x}\n5X SEM JUROS: R${p5x}\n'
              f'6X SEM JUROS: R${p6x}\n7X SEM JUROS: R${p7x}\n8X SEM JUROS: R${p8x}')
        
main()