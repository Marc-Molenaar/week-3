def binair_positie_twee():

    binair = input("Geef een binair getal op: ")

    # Check if input is a binary number else ask again
    while not all(number in "01" for number in binair):
        binair = input("Geef een binair getal op: ")

    binair = str(binair)
    eenen_bij_elkaar = 0

    for number in binair:
        if int(number) == 1:
            eenen_bij_elkaar += 1

    print(eenen_bij_elkaar)


if __name__ == '__main__':
    binair_positie_twee()