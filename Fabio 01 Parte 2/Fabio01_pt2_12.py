def main():
    n = int(input('Digite um numero : '))
    m = n // 1000
    c = (n % 1000) // 100
    d = ((n % 1000) % 100) // 10
    u = ((n % 1000) % 100) % 10
    soma = m + c + d + u
    print(soma)

main()
