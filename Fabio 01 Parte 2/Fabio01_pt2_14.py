def main():
    idade = int(input('Idade em dias = '))
    anos = idade // 365
    meses = (idade % 365) // 30
    dias = (idade % 365) % 30
    print('Essa idade é equivalente a {} Anos {} Meses e {} Dias'.format(anos, meses, dias))

main()
