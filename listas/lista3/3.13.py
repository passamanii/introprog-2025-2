def main():

    calc_a()
    calc_b()


def calc_a():
    
    x = 1
    y = 1
    somatorio = 0

    for i in range(50):
        
        somatorio += x/y

        x += 2
        y += 1

    print(f'O resultado de S(a) é de: {somatorio}')

def calc_b():
    
    x = 1
    y = 50
    somatorio = 0

    for i in range(50):

        somatorio += (2**x)/y

        x += 1
        y -= 1

    print(f'O resultado de S(b) é de: {somatorio}')

main()