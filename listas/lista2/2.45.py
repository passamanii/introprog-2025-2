def main():
    
    peso, planeta = pede_informacoes()
    processa_pedido(peso, planeta)

def pede_informacoes():

    peso = float(input('Informe o peso aqui na terra:'))
    planeta = int(input('Informe o código do planeta:'))

    return peso, planeta

def processa_pedido(peso, planeta):

    if (planeta == 1):
        nome_planeta = 'Mercúrio'
        gravidade_planeta = 0.37
        print('olá')
    elif (planeta == 2):
        nome_planeta = 'Vênus'
        gravidade_planeta = 0.88
    elif (planeta == 3):
        nome_planeta = 'Marte'
        gravidade_planeta = 0.38
    elif (planeta == 4):
        nome_planeta = 'Júpiter'
        gravidade_planeta = 2.64
    elif (planeta == 5):
        nome_planeta = 'Saturno'
        gravidade_planeta = 1.15
    elif (planeta == 6):
        nome_planeta = 'Urano'
        gravidade_planeta = 1.17

    peso_planeta = (peso*gravidade_planeta*10)
    print(f'Uma pessoa que pesa {peso*10}N aqui na Terra, pesa {peso_planeta}N em {nome_planeta}.')

main()