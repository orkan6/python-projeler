talk = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything?")).upper().lower()
k = talk.replace(" ","")

if k == "42" or k == "forty-two" or k == "fortytwo":
    print("Yes")
else :
    print("No")
