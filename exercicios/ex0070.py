vf = v1000 = mpr = 0
mb = ''
np = str(input('Nome do produto: '))
pr = int(input('Valor: '))
mpr = pr
mb = np
r = str(input('quer continuar [S/N]: ')).upper().strip()[0]
vf = vf + pr
if pr >= 1000:
    v1000 = v1000 + 1
if pr > mpr:
    mpr = pr
    mb = np
if r == 'S':
    while True:
        np = str(input('Nome do produto: '))
        pr = int(input('Valor: '))
        r = str(input('quer continuar [S/N]: ')).upper().strip()[0]
        vf = vf + pr
        if pr >= 1000:
            v1000 = v1000 + 1
        if pr < mpr:
            mpr = pr
            mb = np
        if r != 'S':
            break
print(f'total da compra {vf}')
print(f'produtos custando mais de 1000 {v1000}')
print(f'produto mais barato {mb} custando {mpr}')