m = f20 = m18 = 0
while True:
    id = int(input('Idade: '))
    sx = str(input('Sexo [M/F]: ')).upper().strip()[0]
    r = str(input('quer continuar [S/N]: ')).upper().strip()[0]
    if id >= 18: 
        m18 = m18 + 1
    if sx == 'M':
        m = m + 1
    if sx == 'F' and id < 20:
        f20 = f20 + 1
    if r == 'N':
        break
print(f'O tanto de pessoas com mais de dezoito anos é {m18}')
print(f'o tanto de homens são {m}')
print(f'O tanto de mulhere -20 são {f20}')