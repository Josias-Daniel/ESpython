c = float(input('Valor dda compra: R$'))
print('à vista no dinheiro/cheque 1')
print('A vista no Cartão 2')
print('2x no cartão 3')
print('3X ou mais no cartão 4')
f = int(input('Forma de pagamento: '))
if f == 1 :
    v = c - (c * 10 / 100)
elif f == 2:
    v = c - (c * 5 / 100)

elif f == 3:
    v = c + (c * 5 / 100)

elif f == 4:
    v = c + (c * 20 / 100)
print('valor original é de {} e o final de {}.'.format(c,v))