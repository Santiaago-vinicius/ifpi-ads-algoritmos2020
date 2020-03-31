def main():
    d = int(input('Dias = '))
    s = d // 7
    x = d % 7
    print('{} Semanas e {} Dia(s)'.format(s, x))

main()