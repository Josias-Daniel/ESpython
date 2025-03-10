F = str(input('Escreva: ')).upper()

print('A letra A aparece {} vezes'.format(F.count('A')))

print('A letra A aparece na primeira vez na posição {}'.format(F.find('A')+1))

print('A letra A aparece a última vez na posição {}'.format(F.rfind('A')+1))