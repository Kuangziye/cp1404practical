from prac_06.guitar import Guitar

guitars = []

print("My guitars!")

# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

while True:
    name = input("Name: ")
    if name == "":
        break
    year = int(input("Year: "))
    cost = int(input("Cost: $"))
    guitars.append(Guitar(name, year, cost))
    print(f"{name} ({year}) : ${cost} added.")

for i, guitar in enumerate(guitars, 1):
    vintage_string = " (vintage)" if guitar.is_vintage(2023) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
