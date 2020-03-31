def main():
    x, y, z = map(float,input('Notas = ').split())
    a, b, c = map(float,input('Pesos = ').split())
    media = (x * a) + (y * b) + (z * c) / (a + b + c)
    print('Media ponderada = {}'.format(media))

main()
