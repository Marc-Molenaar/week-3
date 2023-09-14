class Fitness:
    def __init__(self):
        self.gender = None
        self.age = None
        self.weight = None
        self.height = None
        self.ask_user_data()

    def ask_user_data(self):
        height = input("\nWat is uw lengte? [centimeters]: ")

        while not height.isdigit():
            height = input("Wat is uw lengte? [centimeters]: ")

        self.height = int(height) / 100

        weight = input("Wat is uw gewicht? [kilogram]: ")

        while not weight.isdigit():
            weight = input("Wat is uw gewicht? [kilogram]: ")

        self.weight = int(weight)

        age = input("Wat is uw leeftijd? [jaren]: ")

        while not age.isdigit():
            age = input("Wat is uw leeftijd? [jaren]: ")

        self.age = int(age)

        gender = input("Wat is uw geslacht? [m/v]: ")

        while gender != "m" and gender != "v":
            gender = input("Wat is uw geslacht? [m/v]: ")

        self.gender = gender

        return True

    def calculate_bmi(self):
        # Bereken BMI
        bmi = int(self.weight) / (self.height * self.height)
        bmi = round(bmi, 2)

        if bmi < 18.5 or bmi > 25:
            return f"\033[91m{bmi}\033[0m 👺"

        else:
            return f"\033[92m{bmi}\033[0m 🤌"

    def calculate_bmr(self):
        if self.gender == "m":
            bmr = 66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age)
        else:
            bmr = 655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)

        return round(bmr, 2)

    @staticmethod
    def calculate_energyusage():

        intensity_percentage = input("Hoe intensief heeft u gesport? [1-100%]: ")

        while not intensity_percentage.isdigit():
            intensity_percentage = input("Hoe intensief heeft u gesport? [1-100%]: ")

        intensity_percentage = int(intensity_percentage)

        duration = input("Hoe lang heeft u gesport? [minuten]: ")

        while not duration.isdigit():
            duration = input("Hoe lang heeft u gesport? [minuten]: ")

        duration = int(duration)

        energyusage = 0.0215 * intensity_percentage * duration

        return round(energyusage, 2)

    def calculate_heartratezone(self):
        # Bereken maximale hartslag
        max_heartbeat = 220 - int(self.age)

        # Vraag naar rusthartslag
        rest_heartbeat = input("Wat is uw rusthartslag? [slagen per minuut]: ")

        while not rest_heartbeat.isdigit():
            rest_heartbeat = input("Wat is uw rusthartslag? [slagen per minuut]: ")

        rest_heartbeat = int(rest_heartbeat)

        # Vraag naar trainingsintensiteit
        training_intensity = input("Wat is uw trainingsintensiteit? [1-100%]: ")

        while not training_intensity.isdigit() and 100 < int(training_intensity) < 1:
            training_intensity = input("Wat is uw trainingsintensiteit? [1-100%]: ")

        training_intensity = int(training_intensity)

        # Berekent hartslagzone
        heartrate_zone = rest_heartbeat + (max_heartbeat - rest_heartbeat) * (training_intensity / 100)

        # Rond af op 0 decimalen
        heartrate_zone = round(heartrate_zone, 0)

        return heartrate_zone
