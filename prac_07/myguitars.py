from guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    guitars.sort()

    for guitar in guitars:
        print(guitar)

    add_guitar(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


# Complete first part of More Guitars exercise
def add_guitar(guitars):
    while True:
        name = input("Name: ")
        if not name:
            break
        year = input("Year: ")
        cost = float(input("Cost: "))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)

        # Append the new guitar to the file
        with open('guitars.csv', 'a') as file:
            file.write(f"\n{new_guitar.name},{new_guitar.year},{new_guitar.cost}\n")


main()
