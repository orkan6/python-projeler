sicaklik = int(input("Sıcaklık değeri girin:\n"))
birim = input("Sıcaklık birimi seçin:\nCelcius için C\nFahrenheit için F\nKelvin için K\n")
def hesap():
    celcius()
    fah()
    kel()
def celcius():
    if "C" in birim:
        fah = (sicaklik*9/5) + 32
        kel = sicaklik + 273.15
        girdi = print(fah,"Fahrenheit\n",kel,"Kelvin")
        return girdi
def fah():
    if "F" in birim:
        cel = (sicaklik-32)*5/9
        kel = (sicaklik+ 459.67)*5/9 
        girdi = print(cel,"Celcius\n",kel,"Kelvin")
        return girdi
def kel():
    if "K" in birim:
        cel = sicaklik - 273.15
        fah = (sicaklik*5/9)+459.67 
        girdi = print(cel,"Celcius\n",fah,"Fahrenheit")
        return girdi
hesap()
