def main():
    custo_fabrica = float(input('Custo de Fábrica : '))
    #porcentagem para distribuidor
    x = custo_fabrica * 0.28
    #porcentagem para impostos
    y = custo_fabrica * 0.45
    #aplicando ao custo da fabrica
    custo_consumidor = x + y + custo_fabrica

    print('O valor total pro consumidor sera {:.2f} R$'.format(custo_consumidor))


main()
