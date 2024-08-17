import random
try:
    level = int(input("Level: "))

    if level <= 0:
        while True:
            level = int(input("Level: "))
            if level > 0:
                break

    sayi = random.randint(1,level)
    guess = int(input("Guess: "))

    if guess > sayi:
        print("Too large!")
        guess = int(input("Guess: "))

    elif guess < sayi:
        print("Too small!")
        guess = int(input("Guess: "))

    else:
        print("Just right!")
except ValueError:
    guess = int(input("Guess: "))



