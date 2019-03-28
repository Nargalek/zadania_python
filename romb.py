wys = int(input("Podaj wysokosc rombu: "))
j=wys
z=0
for i in range(1,wys+1):
    print(' ' * j + '/' + ' ' * z + '\\')
    j-=1
    z+=2
j=1
z-=2
for i in range(1, wys+1):
    print(' ' * j + '\\' + ' ' * z + '/')
    j+=1
    z-=2