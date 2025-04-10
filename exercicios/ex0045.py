import random
import time
item = ('tesoura','papel','pedra')
m = random.randint(0,2)
print('1 = tesoura')
print('2 = papel ')
print('3 = pedra')
e = int(input('Escolha :'))
print('Sua escolha foi {}'.format(item[e]))
print('A do Pc foi {}'.format(item[m]))

if m == 0:
    if e == 0:
        print('EMPATE')

    elif e == 1:
        print('Jogador V')

    elif e == 2:
        print('PC V')

elif m == 1:
    if e == 0:
        print('PC V')

    elif e == 1:
        print('EMPATE')

    elif e == 2:
        print('Jogador V')

elif m == 2:
    if e == 0:
        print('Jogador V')

    elif e == 1:
        print('PC V')

    elif e == 2:
        print('EMPATE')