def main():
    #coletar dados
    anos = int(input('Anos = '))
    meses = int(input('meses = '))
    dias = int(input('Dias = '))
    
    # converter dados
    anos_dias = anos * 365
    meses_dias = meses * 30
    
    #total
    soma = anos_dias + meses_dias + dias

    print('{} Dias'.format(soma))

main()
