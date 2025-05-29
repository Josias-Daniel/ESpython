m = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
p = 0
v2 = 0
for l in range(0, 3):
    for c in range(0, 3):
        m[l][c] = int(input('Número: '))
        if m[l][c] % 2 == 0:
            p = p + m[l][c] 
mv = m[1][0]

for l in range(0, 3):
    v2 = v2 + m[l][1]
for l in range(0, 3):
    if m[1][l] > mv:
        mv = m[1][l]

print(m[0])
print(m[1])
print(m[2])
print(f'A soma de pares é {p}')
print(f'O maior valor da segunda coluna é {mv}')
print(f'A soma da segunda linha é {v2}')