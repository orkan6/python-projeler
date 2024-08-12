try:
    x, y = input("Fraction: ").split("/")
    x = int(x)
    y = int(y)
    z = round(((x/y)*100))

    if 1 >= int((x/y)*100) >= 0:
        print("E")
    elif 100 >= int((x/y)*100) >= 99 :
        print("F")
    elif x>y:
      x, y = input("Fraction: ").split("/")
    else:
        print(f"{z}%")
except (ValueError, ZeroDivisionError):
    x, y = input("Fraction: ").split("/")

