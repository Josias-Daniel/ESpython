n = int(input('Digite um número para converter: '))

v = int(input('Você quer converter para oque: 1 = binaro/ 2 = octal/ 3 = hexadecimal'
':'))

if v == 1:
    print('{} para binario é {}'.format(n, bin(n)[2:]))

elif v == 2:
    print('{} para octal é {}'.format(n, oct(n)[2:]))

elif v  == 3:
    print('{} para hexadecimal é {}'.format(n, hex(n)[2:]))

else:
    print('Valor inválido')