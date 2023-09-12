def naar_decimaal():
    # Geef binair getal op
    binair = input("Geef een binair getal op: ")

    # Blijf loopen als gebruiken geen binair getal opgeeft
    while not all(number in "01" for number in binair):
        binair = input("Geef een binair getal op: ")

    # Change type of binair to string, so it loops for each number
    binair = str(binair)

    # Set a counter
    i = len(binair) - 1

    # Set the decimal variable
    decimal = 0

    # For each number in binair
    for number in binair:
        # Add the result of '(2 ^ position) * number' to the decimal value
        decimal += pow(2, i) * int(number)

        i -= 1

    # Print the final result
    print(f"Het resultaat is: {decimal}")


if __name__ == '__main__':
    naar_decimaal()
