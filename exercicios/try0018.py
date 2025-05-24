galera = []
patu = [0,0]
while True:
    patu.pop(0)
    patu.pop(0)
    patu.insert(0,(input('Pessoal: ')))
    patu.insert(1,(int(input('Idade: '))))
    galera.append(patu[:])
    print(patu)
    print(len(galera))
    print(galera)
    if len(galera) == 5:
        print('Acabouuuuuuu')
        break
for p in galera:
    print(p)
    print(f'Eu sou {galera[1][0]}, e tenho {galera[1][1]} de idade')
    if  p[1] > 18:
        print(p[1])
