from pyfiglet import Figlet
import random,sys


figlet = Figlet()
figlet.getFonts()



if len(sys.argv) == 1:
    fontlar = random.choice(figlet.getFonts())
    figlet.setFont(font= fontlar)

elif len(sys.argv) > 1:
    if sys.argv[1] != "-f":
        if sys.argv[1] != "--font":
            sys.exit("Invalid usage")

    if sys.argv[2] in figlet.getFonts():
        figlet.setFont(font= sys.argv[2])

    else:
        sys.exit("Invalid usage")

else:
        sys.exit("Invalid usage")

girdi = input("Input: ")
print(f"Output: {figlet.renderText(girdi)}")





