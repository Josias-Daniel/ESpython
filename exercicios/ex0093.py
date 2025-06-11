j = {}
j['nome'] = str(input('Nome do Jogador: '))
p = int(input('Quantos jogos ele jogou: '))
gs = []
g = 0
for c in range(0, p):
    gs.append(int(input(f'Gols na {c} partida: ')))
    g = g + gs[c]
j['gols'] = gs
j['total'] = g
print(j)
for k ,v in j.items():
    print(f'no campo {k} tem {v}')
print(f'O jogador zico tem {p} partidas')
for c in range(0, p):
    print(f'Na partida {c}, fez {gs[c]} gols')
