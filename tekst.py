s = input("Podaj string: ")
wynik = ''
i=0
for sub in s:
    if i%2!=0:
        wynik += 2*sub
    else:
        wynik+= sub
    i+=1
print(wynik)