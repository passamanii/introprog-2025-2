def main():

    hour, min, seg = map(int, input('Informe o horário no formato (XX:XX:XX):').split(':')) #map() itera cada valor separado pelo .split(), transformando-os no tipo especificado.
    total_seg = SEG(hour, min, seg)
    print(f'{(hour):02d}:{(min):02d}:{(seg):02d} é equivalente à: {total_seg} segundos.')

def SEG(hour, minute, sec):
    
    result = ((hour*3600)+(minute*60)+(sec))

    return result

main()

