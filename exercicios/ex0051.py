pt = int(input('Primeiro termo: '))
r = int(input('Razão: '))

q = pt

for c in range(0,10, 1):
        print(q, end=(' '))
        q = q + r

print('Acabou com {}'.format(q))

        