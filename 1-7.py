
x=int(input("Podaj rok: "))
if x<1582:
    print("Bledny rok! podaj liczbe wieksza od 1581!")
elif (x%4==0 and x%100!=0) or x%400==0:
    print(x," jest rokiem przestepnym")
else:
    print(x, " nie jest rokiem przestepnym")