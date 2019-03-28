dziesietne = int(input('Podaj liczbe dziesietna: '))
roman = []
while dziesietne > 1000:
	roman.append('M')
	dziesietne -= 1000
while dziesietne > 500:
	roman.append('D')
	dziesietne -= 500
while dziesietne > 100:
	roman.append('C')
	dziesietne -= 100
while dziesietne > 50:
	roman.append('L')
	dziesietne -= 50
while dziesietne > 10:
	roman.append('X')
	dziesietne -= 10
while dziesietne > 5:
	roman.append('V')
	dziesietne -= 5
while dziesietne > 1:
	roman.append('I')
	dziesietne -= 1

for i in roman:
    print(i, end='')