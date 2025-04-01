v = float(input('Valor da casa: '))
s = float(input('Seu sálario: '))
a = float(input('Quantos anos vai pagar: '))

vm = v / (a * 12)

if vm > (s * 30 / 100):
    print('Voce não pode ter esse financiamento')
else:
    print('Financiamento permitido')
    
print('O valor mensal seria de {}'.format(vm))