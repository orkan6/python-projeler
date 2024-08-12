sozluk = {}



while True:
    try:
        market = input("").upper()
    except EOFError:
        for meyve in sorted(sozluk.keys()):
            print(sozluk[meyve],meyve)
        exit()

    if market in sozluk:
        sozluk[market] += 1
    else:
        sozluk[market] = 1


