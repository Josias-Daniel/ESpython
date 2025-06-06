p = {}
p['nome'] = str(input('Nome: '))
p['média'] = float(input('Média: '))
if p['média'] < 5:
    p['situação'] = str('Reprovado')
elif p['média'] >= 5 and p['média'] < 7:
    p['situação'] = str('Recuperação')
elif p['média'] >= 7:
    p['situação'] = str('Aprovado')
for k ,v in p.items():
    print(f'{k} é igual a {v}')