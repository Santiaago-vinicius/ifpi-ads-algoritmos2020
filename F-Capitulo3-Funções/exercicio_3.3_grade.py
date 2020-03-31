def quatro_vezes(s):
    print(s)
    print(s)
    print(s)
    print(s)


def grade(coluna):
    coluna -= 1
    sep_1 = '+ - - - - +'
    sep_2 = '+ - - - - +' * coluna
    separador = sep_1 + sep_2

    meio_1 = '|        |' 
    meio_2 = '        |' * coluna
    meio = (meio_1 + meio_2)


def primeira_linha(separador, meio):
    print(separador)
    quatro_vezes(meio)
    print(separador)


def linhas(separador, meio):
    quatro_vezes(meio)
    print(separador)

grade(5)