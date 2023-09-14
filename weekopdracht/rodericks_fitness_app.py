import classes.fitness as fitness


def main():
    print("Welkom bij de fitness app! 🍩")
    print("Voordat we beginnen hebben we wat gegevens van u nodig.")

    fitness_app = fitness.Fitness()

    running = True

    while running:
        print("\nWat wilt u berekenen?")
        print("1. BMI")
        print("2. BMR")
        print("3. Calorieverbruik")
        print("4. Hartslagzone")
        print("9. Gegevens opnieuw invoeren")

        choice = input("Keuze: ")

        while not choice.isdigit():
            choice = input("Keuze: ")

        if choice == "1":
            print(f"\nUw BMI is: {fitness_app.calculate_bmi()}")

        elif choice == "2":
            print(f"\nUw BMR is: {fitness_app.calculate_bmr()}")

        elif choice == "3":
            print(f"\nUw calorieverbruik is: {fitness_app.calculate_energyusage()}")

        elif choice == "4":
            print(f"\nUw hartslagzone is: {fitness_app.calculate_heartratezone()}")

        elif choice == "9":
            fitness_app.ask_user_data()

        else:
            print("\n\033[91mOngeldige keuze\033[0m")

        choice = input("Wilt u nog een berekening doen? [j/n]: ")

        while choice != "j" and choice != "n":
            choice = input("Ongeldige keuze, probeer opnieuw [j/n]: ")

        if choice == "n":
            running = False

    print("\nBedankt voor het gebruiken van de fitness app! 🦆")


if __name__ == '__main__':
    main()
