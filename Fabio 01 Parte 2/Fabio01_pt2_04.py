def main():
    x = int(input('Segundos = '))
    h = x // 3600
    resto_hora = x % 3600
    minutos = resto_hora // 60
    s = resto_hora % 60
    print('{} h {} m {} s'.format(h, m, s))

main()