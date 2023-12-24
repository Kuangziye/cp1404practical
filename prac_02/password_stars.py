"""
MIN_PASSWORD = 8

function main()
    password = get_password()
    display("*" * len(password))

function get_password()
    get password
     while len(password) < MIN_PASSWORD:
        display "The password length does not meet the requirements"
        get password
    return password

main()

"""

MIN_PASSWORD = 8


def main():
    password = get_password()
    print("*" * len(password))


def get_password():
    password = str(input("Enter your password: "))
    while len(password) < MIN_PASSWORD:
        print("The password length does not meet the requirements")
        password = str(input("Enter your password: "))
    return password


main()
