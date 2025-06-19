import random
def ml(* vals):
    q = 0
    mv = 0
    for val in vals:
        if val > mv:
            mv = val
        q = q + 1 
        print(val, end=' ')
    print(f'. foram informados {q} valores sendo o maior {mv}')


#Progama==================
ml(random.randint(0, 10), random.randint(0, 10), random.randint(0, 10))
ml((random.randint(0, 10)) * random.randint(0, 10))