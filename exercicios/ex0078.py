vals = list()
c = mr = mn = 0
while True:
    c = c + 1
    vals.append(input('número: '))
    if c == 5:
        c = 1
        break
mr = mn = vals[0]
while True:
    if vals[c] > mr:
        mr = vals[c]
    if vals[c] < mn:
        mn = vals[c]
    c = c + 1
    if c == 5:
        break

print(vals)
print(f'O maior valor foi {mr} na posoçaõ:', end=' ')
for p , v in enumerate(vals):
    if v == mr:
        print(f'{p}', end='...')
p = v = 0
print(f'O menor valor foi {mn} na posiçaõ:', end=' ')
for p, v in enumerate(vals):
    if v == mn:
        print(f'{p}', end='...')