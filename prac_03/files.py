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
total = 0
in_file = open("numbers.txt", 'r')
for i in range(0, 2):
    number = in_file.readline()
    total = total + int(number)
print(total)
in_file.close()

# 4.
total = 0
in_file = open("numbers.txt", 'r')
numbers = in_file.readlines()
for number in numbers:
    total += int(number)
print(total)
in_file.close()
