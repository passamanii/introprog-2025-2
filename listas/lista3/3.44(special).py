#Nesse código está presente a fórmula que mencionei no arquivo anterior.
#https://www.mersenne.org

def e_primo(n):

    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def main():

    perfeitos = []
    p = 2

    while len(perfeitos) < 5:

        mersenne = 2**p - 1

        if e_primo(mersenne):
            perfeito = 2**(p-1) * mersenne
            perfeitos.append(perfeito)

        p += 1

    print("Números perfeitos:", *perfeitos)


main()