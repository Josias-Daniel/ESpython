import random
c = 0
j = 0 
m = 0

while c < 3:
    vl = random.randint(1,10)
    r = int(input('Digite um valor: '))
    e = str(input('Você escolhe par[P], ou impar[I]: '))
    soma = vl + r
    print(f'Você colocou {r} e a maquina {vl} isso dá {soma}')
    if e == 'P' and (soma % 2 == 0):
        print('Você ganhou')
        j = j + 1
        c = c + 1
    elif e == 'I' and (soma % 2 == 0):
        print('Você perdeu')
        m = m + 1
        c = c + 1
    elif e == 'P' and (soma % 2 != 0):
        print('Você perdeu')
        m = m + 1
        c = c + 1
    elif e == 'I' and (soma % 2 != 0):
        print('Você ganhou')
        j = j + 1
        c = c + 1
    else:
        print('Tem algo errado, tente de novo')
    print('=' * 30)
print(f'Você ganhou {j} vezes e a maquina {m}')
if j > m :
    print('VOCÊ GANHOU')
else:
    print('VOCÊ PERDEU')