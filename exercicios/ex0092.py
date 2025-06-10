p = {}
p['Nome'] = str(input('Nome:'))
p['Ano de Nascimeto'] = (2025 - int(input('Nascimento: ')))
p['crt'] = int(input('Carteira de Trabalho[0 para não tem]: '))
if p['crt'] != 0:
    p['Idade'] = int(input('Ano de Contratação: '))
    p['Salário'] = int(input('Salário: '))

for k, v in p.items():
    print(f'{k} tem valor de {v}')
