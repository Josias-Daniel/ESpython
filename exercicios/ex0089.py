l = []
n = str()
n1 = n2 = nm = 0
while True:
    n = str(input('Nome: '))
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    nm = (n1 + n2) / 2
    l.append([n, [n1, n2], nm])
    r = str(input('Quer continuar[S/N]: '))
    if r in 'Nn':
        break
for c in range(0, len(l)):
    print(c, end='  *   ')
    print(l[c])
while True:
    r = int(input('Quer ver nota de qual[00 para interromper]: '))
    print(l[r][1])
    if r == 00:
        break