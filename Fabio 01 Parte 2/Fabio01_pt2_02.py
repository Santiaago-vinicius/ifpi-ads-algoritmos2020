def main():
    x = int(input('M = '))
    k = x // 1000
    m = x % 1000
    print('{} Km e {} metros'.format(k, m))

main()