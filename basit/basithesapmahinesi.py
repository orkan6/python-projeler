#Kullanıcıdan iki sayı alarak toplama, çıkarma, çarpma ve bölme işlemlerini gerçekleştiren bir program.
a = int(input("İşlem yapmak istediğiniz ilk sayıyı girin:\n"))
b = int(input("İşlem yapmak istediğiniz ikinci sayıyı girin:\n"))
c = (input("İşlem yapmak istediğiniz operatörü girin:\nToplama için: + \nÇıkarma için: -\nÇarpma için: x\nBölme için: /\n"))
def toplama():
    top = a + b
    return top
def cikarma():
    cikar = a - b
    return cikar
def carpim():
    carp = a * b
    return carp
def bolum():
    bol = a / b
    return bol
def hesap():
    if "+" in c:
       print(float(toplama())) 
    elif c == "-":
       print(float(cikarma()))
    elif c == "x":
       print(float(carpim()))
    elif c == "/":
       print(float(bolum()))
hesap()
