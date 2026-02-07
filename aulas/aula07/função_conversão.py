def conversao(x):

    hora = x // 3600
    minutos = (x % 3600) // 60
    segundos = ((x % 3600) % 60) // 60

    print (f'{hora} horas, {minutos} minutos e {segundos} segundos.')

def main():
    