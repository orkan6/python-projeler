#Girilen bir sayının asal olup olmadığını kontrol eden bir program.
sayi = int(input("Sayı girin:\n"))
if sayi <= 1 :
    print("1'den büyük bir sayı seçin")
elif sayi == 2:
    print("Sayı asal")
for i in range(2,sayi):
    if sayi % i == 0:
        print("Sayı asal değil")
        break
else:
    print("sayı asal ")
