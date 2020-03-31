def main():
    valor_mercadoria = float(input('Valor : '))
    valor_prestação = valor_mercadoria // 3 
    valor_entrada = (valor_mercadoria % 3 ) + valor_prestação
    print('voce vai pagar {}R$ de entrada e as prestações serao de {}R$'.format(valor_entrada, valor_prestação))


main()