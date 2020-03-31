def main():
    a = float(input('variavel A : '))
    b = float(input('variavel B : '))
    c = float(input('variavel C : '))
    d = float(input('variavel D : '))
    e = float(input('variavel E : '))
    f = float(input('variavel F : '))
    #achando x
    numerador_x = (c * e) - (a * f)
    denominador_x = (a * e) - (b * d)
    x = numerador_x / denominador_x
    #achando y
    numerador_y = (a * f) - (c * d)
    denominador_y = (a * e) - (b * d)
    y = numerador_y / denominador_y

    print(f'o valor de x é {x} e de y vale {y}')

main()