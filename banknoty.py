s=int(input("Podaj kwote w postaci liczby calkowitej: "))

sto = s // 100
piec = (s%100)//50
dwa = (s % 100 % 50)//20
dyszka = (s%100%50%20)//10
piatka = (s%100%50%20%10) //5
dwaz = (s%100%50%20%10%5) //2
jedenz = (s%100%50%20%10%5%2) //1

print("Kwote ", s," rozmienimy na banknoty (monety): ")
print("100: ", sto)
print("50: ", piec)
print("20: ", dwa)
print("10: ", dyszka)
print("5: ", piatka)
print("2: ", dwaz)
print("1: ", jedenz)
