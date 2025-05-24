ex = (input('Expressão: '))
vp = []
vq = vq2 = 0
for simb in ex:
    if simb == '(':
        vp.append('(')
        vq2 = vq2 + 1
    elif simb == ')':
        if len(vp) > 0:
            vp.pop(0)
        else:
            vp.append(')')
            vq = vq + 1
            break
print(len(vp))
if len(vp) == 0:
    print('A expressão é válida')
else:
    print('Essa expressão é inválida')