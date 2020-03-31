def main():
    a = int(input('Valor 1 = '))
    b = int(input('Valor 2 = '))
    c = int(input('Valor 3 = '))
    #fazendo a expressao
    r = (a + b) ** 2
    s = (c + b) ** 2
    d = (r + s) // 2

    print(d)

main()
