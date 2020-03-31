def main():
    x , y = map(float, input().split())
    quociente = x / y 
    resto = x % y
    print('Quociente vale {:.2f} resto vale {}'.format(quociente,resto))

main()