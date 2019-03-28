from random import randint
loto = []
while len(loto)<6:
    p=randint(1,49)
    k=0
    for j in range(len(loto)):
        if p == loto[j]:
            k=1
    if k == 0:
        loto.append(p)
    
for i in loto:
    print(i)