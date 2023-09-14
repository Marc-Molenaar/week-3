def naar_decimaal():
    # Geef binair getal op
    binair = input("Geef een binair getal op: ")

    # Blijf loopen als gebruiken geen binair getal opgeeft
    while not all(number in "01" for number in binair):
        binair = input("Geef een binair getal op: ")

    # Verander de type van binair naar string
    binair = str(binair)

    # Zet een teller
    i = len(binair) - 1

    # Zet een decimaal variabel
    decimal = 0

    # Voor elk nummer in binair
    for number in binair:
        # Voeg het resultaat van '(2 ^ position) * number' toe aan de decimal waarde
        decimal += pow(2, i) * int(number)

        i -= 1

    # Print het resultaat
    print(f"Het resultaat is: {decimal}")


if __name__ == '__main__':
    naar_decimaal()
