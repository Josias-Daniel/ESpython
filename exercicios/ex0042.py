n1 = float(input('Número 1: '))
n2 = float(input('Número 2: '))
n3 = float(input('Número 3: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('Dá pra formar')

    if n1 == n2 and n2 == n3:
        print('É Equilatero')

    elif n1 != n2 != n3 and n3 != n1:
        print('Escaleno')
    
    else :
        print('Isóceles')


else:
    print('Não dá pra formar')

