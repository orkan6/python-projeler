tw = input("Input: ")
vowel = ["a", "e", "i", "o", "u","A","E","I","O","U"]

l1 = []

for letter in tw:
    if letter not in vowel:
        l1.append(letter)

tw = ''.join(l1)

print(tw)
