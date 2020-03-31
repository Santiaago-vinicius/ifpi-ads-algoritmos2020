def main():
    minutos = int(input('Minutos = '))
    minuto_pra_dia = minutos // 1440
    resto_dias = minutos // 60
    resto_horas = minutos % 60
    print('{} Dias {} horas {} minutos'.format(minuto_pra_dia, resto_dias,resto_horas))

main()