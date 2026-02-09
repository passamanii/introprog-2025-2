def main():

    chico = 1.5
    ze = 1.1
    ano = 0 

    while (1):

        if (ze > chico):

            break

        chico += 0.02
        ze += 0.03
        ano += 1

    
    print(f'- Chico tem {(chico):.2f}m e Zé tem {(ze):.2f}m.\n- Levaram-se {ano} anos para Zé passar Chico em altura.')


main()