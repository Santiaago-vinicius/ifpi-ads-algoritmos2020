def main():
    x = int(input('Número : '))
    C = x // 100
    D = x % 100 // 10
    U = x % 10
    print('{}{}{}'.format(U,D,C))
main()