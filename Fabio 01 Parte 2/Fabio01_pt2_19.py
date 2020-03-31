def main():
    from math import pow
    #primeiro ponto
    x_ponto1 = float(input('x1 : '))
    y_ponto1 = float(input('y1 : '))
    #segundo ponto
    x_ponto2 = float(input('x2 : '))
    y_ponto2 = float(input('y2 : '))
    #formula
    a = (x_ponto2 - x_ponto1) **2
    b = (y_ponto2 - y_ponto1) **2
    d = a + b
    resultado = (d) **(1/2)

    print(f'{resultado:.2f}')


main()