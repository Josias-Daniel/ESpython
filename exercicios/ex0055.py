cq = 0
menor = 1000
maior = 0
for c in range(1, 5+1, 1):
    cq = cq + 1
    pat = float(input('Peso da {}* pessoa: '.format(cq)))
    if pat > maior:
        maior = pat
    elif pat < menor:
        menor = pat
print('O maior peso foi de {} e o menor foi de {}.'.format(maior, menor))
