rn = [[],[]]

for c in range(1, 7 + 1):
    r = int(input(f'{c}*Número: '))
    if r % 2 == 0:
        rn[0].append(r)
    elif r % 2 != 0:
        rn[1].append(r)
print(f'Valores: {rn}')
print(f'Os números pares são {rn[0]}')
print(f'Os números impares são {rn[1]}')