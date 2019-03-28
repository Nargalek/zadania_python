wys = int(input("Podaj wysokosc choinki: "))
j=wys
for i in range(0,wys+1):
    print(' ' * j + '*' * i + '*' * (i-1))
    j-=1
    