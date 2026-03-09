def main():

    total_seg = int(input('Informe o tempo total em segundos:'))
    horario = HMS(total_seg)
    print(f'{total_seg} segundos equivale à: {horario}.')

def HMS(seconds):

    hour = (seconds//3600)
    min = ((seconds%3600)//60)
    sec = ((seconds%3600)%60)

    return (f'{(hour):02d}:{(min):02d}:{(sec):02d}')

main()