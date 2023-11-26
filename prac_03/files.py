# 1.
name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(f"Your name is {name}", file=out_file)
out_file.close()

# 2.
in_file = open("name.txt", 'r')
new_name = in_file.read()
print(f"{new_name}")
in_file.close()

# 3.
out_file = open("numbers.txt", 'w')
print("17\n42\n400", file=out_file)
out_file.close()

in_file = open("numbers.txt", 'r')
lines = in_file.readlines()
number_one = int(lines[0].strip())
number_two = int(lines[1].strip())
result = number_one + number_two
print(f"{result}")
in_file.close()

# 4.
in_file = open("numbers.txt", 'r')
file_number = [int(lines) for lines in in_file]
total = sum(file_number)
print(f"The total number is: {total}")