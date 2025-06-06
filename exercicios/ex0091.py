import random
import operator
jogo = {
'jogador1': random.randint(1, 6),
'jogador2': random.randint(1, 6),
'jogador3': random.randint(1, 6),
'jogador4': random.randint(1, 6)
}
rk = []
print(jogo)
for k ,v in jogo.items():
    print(f'{k} tirou {v}')

rk = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print(rk[0][0],rk[1],rk[2],rk[3])
for p, v in enumerate(rk):
    print(f'{p+1}* lugar: {v[0]} com {v[1]}')


