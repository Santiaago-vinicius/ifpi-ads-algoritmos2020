def main():
    n = int(input('Numero = '))
    #tirando as bases
    m = n // 1000
    c = (n % 1000) // 100
    d = ((n % 1000) % 100) // 10
    u = ((n % 1000) % 100) % 10
    
    #fazendo as contas
    a = m * 8
    b = c * 4
    c = d * 2
    x = u * 1
    s = a + b + c + x

    print('Esse numero na base decimal vale {}'.format(s))

main()