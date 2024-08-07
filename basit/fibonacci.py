#Girilen bir sayının asal olup olmadığını kontrol eden bir program.
sayi = int(input("Sayı girin:\n"))
if sayi <= 0 :
    print("Pozitif bir sayı girin")
fib = [1,1]

while fib[-1] <= sayi:
    fib.append(fib[-1] + fib[-2])
print(fib)
