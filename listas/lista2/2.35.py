def main():
    
    saldo_medio = float(input('(BANCO NÓIS PEGA SEU DINDIN) Informe o saldo médio do cliente ano passado:'))

    if (saldo_medio <= 200):
        credito = saldo_medio * 0
    elif (saldo_medio <= 400):
        credito = saldo_medio * 0.2
    elif (saldo_medio <= 600):
        credito = saldo_medio * 0.3
    else:
        credito = saldo_medio * 0.4
    
    print(f'Fulano de Souza, de saldo médio R${saldo_medio}, foi concebido com um crédito de R${credito}.')

main()