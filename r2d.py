roman = input('podaj liczbe Rzymska: ')
wynik = 0
for i in roman:
    if (i == 'I'): 
        wynik+= 1
    if (i == 'V'): 
        wynik+= 5
    if (i == 'X'): 
        wynik+= 10
    if (i == 'L'): 
        wynik+= 50
    if (i == 'C'): 
        wynik+= 100
    if (i == 'D'): 
        wynik+= 500
    if (i == 'M'): 
        wynik+= 1000
        
print("Liczba dziesietna: ", wynik)