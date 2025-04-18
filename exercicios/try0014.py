for c in range(1, 10+1, 1):
    print('Oi',c)


c2 = 0
while c2 < 10:
    c2 = c2 + 1
    print('OI',c2)
c3 =0
while not c3 == 10:
    c3 = c3 + 1
    print('ioi',c3)
print(c3)
n = 1
while n != 0:
    n = int(input('Valor: '))
print('Fim')
n2 = 1
np = 0
nip = 0
while n2 != 0:
    n2 = int(input('Valor: '))
    if n2 != 0:
        if n2 % 2 == 0:
            np = np + 1
        else:
            nip = nip + 1
print('O tanto de números pares foi {} e números impares foi {}'.format(np,nip))