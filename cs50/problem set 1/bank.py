greet = input("Greeting: ").upper().lower().replace(" ","")
if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h"):
    print("$20")
else:
    print("$100")
