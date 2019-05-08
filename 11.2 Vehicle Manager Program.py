class Cars:
    def __init__(self, brand, model, mileage, service_date):
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.service_date = service_date

    def get_full_name(self):
        return self.brand + " " + self.model


def list_all_cars(cars):
    for index, car in enumerate(cars):
        print("ID: " + str(index))  # index is an order number of the contact object in the contacts list
        print(car.get_full_name())
        print(car.mileage)
        print(car.service_date)
        print("")  # empty line

    if not Cars:
        print("You don't have any contacts in your contact list.")


def add_new_car(cars):
    brand = input("Please enter car brand: ")
    model = input("Please enter car model: ")
    mileage = input("Please enter car mileage: ")
    service_date = input("Please enter cars Service Date: ")

    new = Cars(brand=brand, model=model, mileage=mileage, service_date=service_date)
    cars.append(new)

    print("")  # empty line
    print(new.get_full_name() + " was successfully added to the list of cars.")


def edit_car(cars):
    print("Select the number of the contact you'd like to edit:")

    for index, car in enumerate(cars):
        print(str(index) + ") " + car.get_full_name())

    print("")  # empty line
    selected_id = input("What car would you like to edit? (enter ID number): ")
    selected_car = cars[int(selected_id)]

    new_mileage = input("Please enter new mileage for %s: " % selected_car.get_full_name())
    selected_car.mileage = new_mileage

    new_service_date = input("Please enter new service date for %s: " % selected_car.get_full_name())
    selected_car.service_date = new_service_date

    print("")  # empty line
    print("Mileage and Service Date updated.")
    # ... you can do the same for other fields.


def delete_car(cars):
    print("Select the number of the contact you'd like to delete:")

    for index, car in enumerate(cars):
        print(str(index) + ") " + car.get_full_name())

    print("")  # empty line
    selected_id = input("What contact would you like to delete? (enter ID number): ")
    selected_car = cars[int(selected_id)]

    cars.remove(selected_car)
    print("")  # empty line
    print("Contact was successfully removed from your cars list.")


def main():
    # First cars are hardcoded
    car1 = Cars(brand="Buick", model="Van", mileage="12000", service_date="2016")
    car2 = Cars(brand="Volvo", model="v220", mileage="14000", service_date="2018")
    car3 = Cars(brand="Mercedes", model="E500", mileage="16000", service_date="2017")
    cars = [car1, car2, car3]

    while True:
        print("")  # empty line
        print("Please choose one of these options:")
        print("a) See all your cars")
        print("b) Add a new car")
        print("c) Edit a car")
        print("d) Delete a car")
        print("e) Quit the program.")
        print("")  # empty line

        selection = input("Enter your selection (a, b, c, d or e): ")
        print("")  # empty line

        if selection.lower() == "a":
            list_all_cars(cars)
        elif selection.lower() == "b":
            add_new_car(cars)
        elif selection.lower() == "c":
            edit_car(cars)
        elif selection.lower() == "d":
            delete_car(cars)
        elif selection.lower() == "e":
            print("Thank you for using The Vehicle Manager Program. Goodbye!")
            break
        else:
            print("Sorry, I didn't understand your selection. Please try again.")
            continue


if __name__ == "__main__":
    main()
