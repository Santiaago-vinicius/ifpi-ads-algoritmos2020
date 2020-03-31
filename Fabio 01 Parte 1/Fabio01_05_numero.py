def main():
    X = int(input('Numero >> '))
    C = X // 100
    D = X % 100 // 10 
    U = X % 10 
    print('{} Centenas {} Dezenas e {} Unidades '.format(C, D, U))
main()