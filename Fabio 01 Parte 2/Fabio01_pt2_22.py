def main():
    valor = int(input('Valor solicitado = '))
    notas_50 = valor // 50
    notas_10 = (valor % 50) // 10
    notas_5 = ((valor % 50) % 10) // 5
    notas_1 = ((valor % 50) % 10) % 5

    print('Voce pediu {} R$, vai receber {} notas de 50, {} notas de 10, {} notas de 5 e {} notas de 1'.format(valor, notas_50, notas_10, notas_5, notas_1))


main()