import datetime
n = int(input('idade de nascimento: '))
i = datetime.date.today().year - n

print(i)
if i < 9 :
    print('MIRIN') 

elif i >= 9 and i < 14:
    print('INFANTIL')

elif i >= 14 and i < 19:
    print('JUNIOR')

elif i >= 19 and i < 25:
    print('SENIOR')

else:
    print('MASTER')