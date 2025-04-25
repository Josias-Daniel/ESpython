f = 0
c = 0
n = int(input('Coloque um valor para somar [999 para encerrar]: '))
while n != 999:
    f = f + n
    c = c + 1
    n = int(input('Coloque um valor para somar [999 para encerrar]: '))
print('O resultado foi {} com {} números'.format(f,c))
f = 0
