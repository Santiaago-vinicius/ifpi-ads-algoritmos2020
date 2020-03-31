def main():
   #Entrada
    anos = int(input('Quantos anos ele fumou : '))
    cigarros = int(input('cigarros fumados : '))
    preço_carteira = float(input('Preço da carteira : '))

    #transformando 
    dias = anos * 365
    total_cigarros = dias * cigarros
    carteira_compradas = total_cigarros / 20
    total = carteira_compradas * preço_carteira

    print('Ele gastou um total de {:.2f}R$'.format(total))

main() 