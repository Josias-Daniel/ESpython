n = int(input('final: '))
i = int(input('inicio: '))
p = int(input('passo '))

s = 0
for c in range(i, n+1, p):
    nr = int(input('num'))
    s = s + nr
    print(c)
print('By Word')
print(s)