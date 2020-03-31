def main():
    meses = int(input('Meses = '))
    meses_para_anos = meses // 12
    resto_meses = meses % 12
    print('{} Ano(s) e {} mese(s)'.format(meses_para_anos, resto_meses))

main()
