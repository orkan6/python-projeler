def main():
    talk = str(input("Talk:\n"))
    converted = emoji(talk)
    print(converted)

def emoji(talk):
    happy = talk.replace(":)", "🙂")
    sad = happy.replace(":(", "🙁")
    return sad

main()
