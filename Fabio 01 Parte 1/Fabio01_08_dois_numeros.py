def main():
    X , Y = map(int, input('Números : ').split())
    Soma = X + Y
    Sub = X - Y
    Divide = Soma / Sub
    print('Resultado = {:.2f}'.format(Divide))
main()