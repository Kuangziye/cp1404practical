from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(gibson)
another_guitar = Guitar("Another Guitar", 2013)
print(another_guitar)

print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age(2022)}")
print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age(2022)}")
print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(2023)}")
print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(2023)}")