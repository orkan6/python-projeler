import inflect
p = inflect.engine()
isimler = []
try:
    while True:
        isim = input("Name: ")
        isimler.append(isim)


except EOFError:
    liste = p.join(isimler)
    print("Adieu, adieu, to "+liste)
