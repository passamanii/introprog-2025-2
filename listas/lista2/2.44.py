def main():

    mes, numero = pede_informacoes()
    processa_vencimento(mes, numero)

def pede_informacoes():

    actual_month = input('Informe o mês atual:').upper()
    plate_number = int(input('Informe os números da placa do veículo:'))

    return actual_month, plate_number

def processa_vencimento(month, plate_number):

    if (plate_number % 10 == 1):
        expiration_month = 'JANEIRO'
    elif (plate_number % 10 == 2):
        expiration_month = 'FEVEREIRO'
    elif (plate_number % 10 == 3):
        expiration_month = 'MARÇO'
    elif (plate_number % 10 == 4):
        expiration_month =  'ABRIL'
    elif (plate_number % 10 == 5):
        expiration_month = 'MAIO'
    elif (plate_number % 10 == 6):
        expiration_month = 'JUNHO'
    elif (plate_number % 10 == 7):
        expiration_month = 'JULHO'
    elif (plate_number % 10 == 8):
        expiration_month = 'AGOSTO'
    elif (plate_number % 10 == 9):
        expiration_month = 'SETEMBRO'
    
    if (expiration_month == month):
        print(f'O vencimento do IPVA do veículo de placa {plate_number} é esse mês({month}).')
    else:
        print(f'O vencimento do IPVA do veículo de placa {plate_number} é {expiration_month}.')
    
main()
    