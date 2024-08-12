print("Amount Due: 50")
c = int(input("Insert Coin: "))

coin = []
coin.append(c)
a = 50 - c

if 25 in coin or 10 in coin or 5 in coin:
    while (a) != 0:
        print("Amount Due:", a)
        a -= int(input("Insert Coin: "))
        if a == 0:
            print("Change Owed: 0")
        elif a < 0 :
            print("Change Owed:", a*(-1))
            break



elif 50 in coin:
    print("Change Owed: 0")

else:
    print("Amount Due: 50")
