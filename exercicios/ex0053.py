f = str(input('Nome de: ')).strip().upper()

p = f.split()

tj = ''.join(p)

ct = ''

for l in range(len(tj) -1, -1, -1):
    ct = ct + tj[l]

print(ct)

if tj == ct :
    print('{} É um palindromo'.format(ct))
else:
    print('{} Não é um palindromo'.format(ct))

