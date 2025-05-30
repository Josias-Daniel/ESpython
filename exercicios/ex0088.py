import random
l = [[],[]]
r = int(input('Rodadas: '))
for p in range(0 , r):
    for c in range(0, 6):
        l[p][c] = random.randint(1, 60)
for c in range(0, r):
    print(f'Jogo {c+1}: {l[c]}')