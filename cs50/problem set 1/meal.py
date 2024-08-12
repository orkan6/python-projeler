def main():
    clock = input("What time is it? ")
    time = convert(clock)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")

def convert(time):
    hours, minute = time.split(":")
    a = int(hours) + float(minute)/60
    return a



if __name__ == "__main__":
    main()
