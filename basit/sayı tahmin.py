import random
random.randint(0,100)
sayi = int(input("0-100 arasında bir sayı tahmin edin:\n"))
if sayi == random.randint(0,100):
    print("Doğru tahmin")
else:
    print("Yanlış tahmin")
