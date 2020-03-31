def main():
    quantidade_horas = int(input('Horas = '))
    semanas = quantidade_horas // 168
    resto_horas = quantidade_horas % 168
    d = x // 24
    h = d %  24
    print('{} Semanas {} Dias {} Horas'.format(s, d, h))

main()