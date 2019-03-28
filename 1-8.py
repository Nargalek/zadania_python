from random import randint
los = [0,0,0]
while True:
    for i in range(0,3):
        los[i] = randint(0,9)
        print(los[i], "\t", end="")
    print()
    if los[0]==los[1] and los[0]==los[2]:
        print("3 liczby sa takie same!")
    elif los[0]==los[1] or los[0]==los[2] or los[1]==los[2] and (los[0]!=los[1] and los[0]!=los[2]):
        print("2 liczby sa takie same!")
    c = input("Wcisnij T aby zakonczyc, enter aby kontynuowac ")
    if c is "t":
        break