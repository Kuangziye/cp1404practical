"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

"1.A: When the user's input type is not int type, the ValueError will occur."
"2.A: When the user input denominator is 0, the ZeroDivisionError will occur."
"3.A: Yes, I could. I would like to change the code like this:"
numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))
while denominator == 0:
    print("Please input a valid denominator")
    denominator = int(input("Enter the denominator: "))
fraction = numerator / denominator
print(fraction)


