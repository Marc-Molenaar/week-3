def vraag_naam():
    naam = input("Wat is je naam? ")
    return naam


def vraag_leeftijd():
    leeftijd = input("Wat is je leeftijd? ")
    return leeftijd


def vraag_favoriete_programmeertaal():
    programmeertaal = input("Wat is je favoriete programmeertaal? ")
    return programmeertaal


def toon_informatie():
    naam = vraag_naam()
    leeftijd = vraag_leeftijd()
    favoriete_programmeertaal = vraag_favoriete_programmeertaal()

    print(f"Hallo {naam}, jij bent {leeftijd} jaar oud en je favoriete programmeertaal is {favoriete_programmeertaal}")


if __name__ == '__main__':
    toon_informatie()
