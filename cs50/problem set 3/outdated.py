months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    tarih = input("Date: ").strip()

    if "/" in tarih:
        try:
            ay, gun, yil = tarih.split("/")
            ay = int(ay)
            gun = int(gun)
            yil = int(yil)
        except ValueError:
            continue

    elif "," in tarih:
        try:
            a = tarih.replace(",", "")
            ay, gun, yil = a.split(" ")
            gun = int(gun)
            yil = int(yil)

            if ay in months:
                ay = months.index(ay) + 1
            else:
                continue  # Geçerli bir ay değilse tekrar sor
        except ValueError:
            continue  # Eğer sayılara çevrilmezse yeniden sor
    else:
        continue  # Geçerli formatta değilse yeniden sor

    # Ay ve gün değerlerinin geçerliliğini kontrol et
    if gun > 31 or ay > 12 or gun < 1 or ay < 1:
        continue
    else:
        break

print(str(yil) + "-" + "{:02d}".format(ay) + "-" + "{:02d}".format(gun))






