def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def start(plate):
    if plate[0:2].isalpha() == True and plate.isalnum() == True:
        return True
    else:
        return False

def length(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        return False

def pos(plate):

    for i in plate:
        poz = plate.index(i)

        if i.isdigit() == True:

            if plate[poz:].isdigit() == True and int(plate[poz]) !=0:

                return True

            else:
                return False
    if plate.isalpha() == True or plate[poz:].isalpha() == False:
        return True



def is_valid(s):
    if start(s) == True and length(s) == True and pos(s) == True :
        return True
    else:
        False


main()
