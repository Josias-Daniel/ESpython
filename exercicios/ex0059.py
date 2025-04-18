v1 = int(input('Valor número 1: '))
v2 = int(input('Valor número 2: '))
r = 0
while not r == 5:
    print('1 = soma')
    print('2 = multiplicar')
    print('3 = maior')
    print('4 = novos números')
    print('5 = sair do programa')
    r = int(input('O que você quer fazer: '))

    if r == 1:
        print(' a soma de {} e {} é {}'.format(v1, v2,(v1 + v2)))

    elif r == 2:
        print('a multiplicação de {} e {} é {}'.format(v1, v2,(v1 * v2)))

    elif r == 3:
        if v1 < v2:
            print('O maior é {}'.format(v2))
        else:
            print('O maior é {}'.format(v1))

    elif r == 4:
        print('Diga os números novamente')
        v1 = int(input('Valor 1: '))
        v2 = int(input('Valor 2: '))

    elif r == 5:
        print('Môro, até mais menó')

    else:
        print('Resposta inválida.')

print('Falou seu panela de arroixxxxx kkkk')