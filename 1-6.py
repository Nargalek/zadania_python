
x=float(input("Podaj ilosc sekund: "))
g = x // 3600
x = x%3600
m = x // 60
x %= 60
print("czas: ", int(g), "g ", int(m),"m ", int(x),"s")