j = {}
js = []
c = 0
while True:
    j['nome'] = str(input('Nome do Jogador: '))
    p = int(input('Quantos jogos ele jogou: '))
    gs = []
    g = 0
    for c in range(0, p):
        gs.append(int(input(f'Gols na {c} partida: ')))
        g = g + gs[c]
    j['gols'] = gs
    j['total'] = g
    r = str(input('Quer contiar[S/N]: '))
    js.append(j.copy())
    c = c + 1
    if r in 'Nn':
        break
while True:
    rs = int(input('qual jogador você quer ver[999 para]: '))
    if rs == 999:
        break
    print(js[rs])
print(js)
