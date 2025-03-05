N = str(input('Nome: '))

print(len(N))

print(('O tanto de Letras s é '),N.count('s'))

print(N.find('a')) 

print('Jo' in N)

N = N.replace('Jo', 'Go')
print (N) 

print(N.upper())

print(N.lower())

print (N.capitalize())

print (N.title())

print(N.strip())

print(N.lstrip())

print(N.rstrip())

print(N.split())

print('-'.join(N))