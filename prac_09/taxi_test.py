from car import Car
from taxi import Taxi


def main():
    prius = Taxi("Prius 1", 100)

    prius.drive(40)

    print(prius)

    prius.start_fare()
    prius.drive(100)

    print(prius)


main()
