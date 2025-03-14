nk = float(input('Número de Km : '))
if nk >= 200:
    p = nk * 0.45
else:
    p = nk * 0.50
print('O valor será de {}R$'.format(p))