nums = ('zero', 'um','dois', 'três', 'quatro', 'cinco', 'seis', 'sete,', 'oito', 'nove,', 'dez', 
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeses', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    es = int(input('número escolhido: '))
    if es < 0  or es > 20:
        print('algo errado tente novamente')
    else:
        print(f'O número escolhido foi {nums[es]}')
        r =str(input('CONTINUAR: [S/N]'))
        if r == 'N':
            break
print(f'O número escolhido foi {nums[es]}')
