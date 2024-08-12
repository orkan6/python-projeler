
d = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

try:
    x = input("Item: ").title()
except EOFError:
      exit()

total = 0


while True:
    if x in d:
          z = float(d[x])
          total += d[x]
          print(f"Total: ${total:.2f}")
          x = input("Item: ").title()


    else:
         x = input("Item: ").title()
