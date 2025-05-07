v = int(input('Digite um valor: '))
while True: 
    r = int(input('Digite um valor: '))
    if r == 999:
        break
    v = v + r
print(f'A soma dos números é {v}')