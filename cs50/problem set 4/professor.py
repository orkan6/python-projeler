import random

#11/12

def main():
    level = get_level()
    generate_integer(level)


def get_level():
    try:
        gecerli = [1,2,3]
        level = int(input("Level: "))
        while level not in gecerli:
                level = int(input("Level: "))
                if level in gecerli:
                    break
        return level
    except ValueError:
        level = int(input("Level: "))
        return level


def generate_integer(level):
    sayac = 0
    yanlis = 0
    dogru = 0
    cevap = []
    if level == 1:
        while dogru < 10:
            x = random.randint(0, 10)
            y = random.randint(0, 10)
            soru = input(f"{x} + {y} = ")

            if int(soru) != x+y:
                cevap.append(x+y)
                print("EEE")
                yanlis += 1

                if yanlis == 3:
                    print (cevap[0])
                    if yanlis == 6:
                        print(cevap[3])

            elif int(soru) == x+y:
                dogru += 1
        sayac = dogru - yanlis
        print(f"Score: {sayac}")

    elif level == 2:
        for i in range (1,11):
            x = random.randint(10, 100)
            y = random.randint(10, 100)
            soru = input(f"{x} + {y} = ")

            if int(soru) != x+y:
                print("EEE")
                cevap.append(x+y)
                yanlis += 1
                if yanlis == 3:
                    print (cevap[0])
                    if yanlis == 6:
                        print(cevap[3])
            elif int(soru) == x+y:
                sayac += 1
        print(f"Score: {sayac}")

    elif level == 3:

        for i in range (1,11):
            x = random.randint(100, 1000)
            y = random.randint(100, 1000)
            soru = input(f"{x} + {y} = ")

            if int(soru) != x+y:
                cevap.append(x+y)
                print("EEE")
                yanlis += 1
                if yanlis == 3:
                    print (cevap[0])
                    if yanlis == 6:
                        print(cevap[3])
            elif int(soru) == x+y:
                sayac += 1
        print(f"Score: {sayac}")
    else:

            level = input("Level: ")




if __name__ == "__main__":
    main()
