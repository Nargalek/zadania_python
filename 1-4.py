
print("Podaj liczbe calkowita wieksza od 2: ")
x=int(input())
y=0
if x>2:
    for i in range(1,x+1):
        if i%2==0:
            y+=i
            
    print("Suma liczb parzystych: ", y)
else:
    print("BLAD ! Liczba musi byc wieksza od 2")