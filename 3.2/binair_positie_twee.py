def binair_positie_twee(binair):

    binair = str(binair)
    i = len(binair) - 1

    for number in binair:
        print(pow(2, i))
        i -= 1


if __name__ == '__main__':
    binair_positie_twee(101011101)
