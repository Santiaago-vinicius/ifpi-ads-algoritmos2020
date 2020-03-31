def main():
    M = float(input('Minutos >> '))
    Horas =  M / 60
    Minutos = M % 60
    print('{:.1f} Horas e {} Minutos'.format(Horas,Minutos))
main()