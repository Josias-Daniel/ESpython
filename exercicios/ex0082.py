l = []
lm = []
lp = []
while True:
    rn = int(input('Número: '))
    r = str(input('Continuar[S/N]: '))
    l.append(rn)
    if rn % 2 == 0:
        lp.append(rn)
    else:
        lm.append(rn)
    if r in 'Nn':
        break
print(f'A lista é {l}')
print(f'Os pares são {lp}')
print(f'Os impares são {lm}')

    