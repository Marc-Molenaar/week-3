def binair_to_string(binair):
    string = ""
    for number in str(binair):
        string += number

    print(string)


if __name__ == '__main__':
    binair_to_string(101011101)
