p1 = int(input('Primeiro termo: '))
r2 = int(input('Razão: '))
t = p1
c = 1
tot = 0
mais = 10
while mais != 0:
    tot = (tot + mais)
    while c <= tot:
        print('{} --D '.format(t), end=(''))
        t += r2
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais: '))

print('FIM')