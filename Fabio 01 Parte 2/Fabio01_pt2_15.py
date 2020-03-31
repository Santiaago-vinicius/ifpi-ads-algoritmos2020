def main():
    #Fração 1 
    n1 = int(input('numerador fração 1 = '))
    d1 = int(input('denominador fração 1 = '))

    #Fração 2
    n2 = int(input('numerador fração 2 = '))
    d2 = int(input('denominador fração 2 = '))

    #somando
    numerador_final = (d2 * n1) + (d1 * n2)
    denominador_final = d1 * d2
    print(f'a soma das frações vale {numerador_final}/{denominador_final}')

main()
