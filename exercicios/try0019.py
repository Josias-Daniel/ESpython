dados = {'nome':'Josias','idade':15,'sexo':'M'}
dados2 = {'nome':'Julia','idade':'15','sexo':'F',}
nomes = []
nomes.append(dados)
nomes.append(dados2)
print(dados.values())
print(dados.keys())
for k, v in dados2.items():
    print(f'O {k} é {v}') 
print(nomes)
print(nomes[1]['nome'])

print('=' * 30)
c = 0
br = []
es = {}
for c in range(0, 2):
    es['n'] = str(input('Nome do estado: '))
    es['sigla'] = str(input('Sigla: '))
    br.append(es.copy())
for e in br:
    for v in e.values(): 
        c = c + 1
        if c % 2 == 0:
            print(f'{v}', end=':    ')
        elif c % 2 != 0:
            print(v) 
        