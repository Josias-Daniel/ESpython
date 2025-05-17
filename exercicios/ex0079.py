nums = []
r = str
while True:
    n = input('Número: ')
    if n not in nums:
        nums.append(n)
        r = str(input('Continuar [S/N]: '))
        if r in 'Nn':
            break
    else:
        print('Número ja ta na lista vacilão tenta de novo')
print(f'Seus números são {nums}')
