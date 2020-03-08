def print_menu():
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilograms to Paunds")
    print("4. Paunds to Kilograms \n")


def km_miles():
    km = float(input("Enter distance in Kilometers: "))
    miles = km / 1.609
    print(f"Distance in miles: {miles}")

def miles_km():
    miles = float(input("Enter distance in Kilometers: "))
    km = miles * 1.609
    print(f"Distance in miles: {km}")

def kg_paunds():
    kg = float(input("Enter weights in Kilograms: "))
    paunds = kg * 2.205
    print(f"weights in Paunds: {paunds}")

def paunds_kg():
    paunds = float(input("Enter weights in Kilograms: "))
    kg = paunds / 2.205
    print(f"weights in Kilograms: {kg}")


if __name__ == "__main__":
    print_menu()
    choise = input("Which conversation would you like to do?: \n")
    if choise == "1":
        km_miles()
    if choise == "2":
        miles_km()
    if choise == "3":
        kg_paunds()
    if choise == "4":
        paunds_kg()