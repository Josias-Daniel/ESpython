s = 0
cont = 0
for c in range(1, 500+1, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
    print(c, end=(' '))
print('A soma deu {}'.format(s))
print('O tanto de números usados uteis disso foram: {}'.format(cont))