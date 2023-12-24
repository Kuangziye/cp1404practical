"""
choice_menu = "(G)et\n(P)rint\n(S)how\n(Q)uit"

function main():
    score = 0
    display choice_menu
    get choice
     while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            level = choose_score_level(score)
            print(level)
        else:
            stars = show_stars(score)
            print(stars)
        choice = str(input("Enter your choice:")).upper()
    display Thanks for using

function get_score():
    score = int(input("Enter score<0>-<100>:"))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score:"))
    return score

function choose_score_level(grade):
    if grade > 100:
        level = "Invalid score"
    elif grade > 90:
        level = "Excellent"
    elif grade >= 50:
        level = "Passable"
    else:
        level = "Bad"
    return level

function show_stars(score):
    stars = "*" * score
    return stars

"""
choice_menu = "(G)et\n(P)rint\n(S)how\n(Q)uit"


def main():
    score = 0
    print(choice_menu)
    choice = str(input("Enter your choice:")).upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            level = choose_score_level(score)
            print(level)
        else:
            stars = show_stars(score)
            print(stars)
        choice = str(input("Enter your choice:")).upper()
    print("Thanks for using")


def get_score():
    score = int(input("Enter score<0>-<100>:"))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score:"))
    return score


def choose_score_level(grade):
    if grade > 100:
        level = "Invalid score"
    elif grade > 90:
        level = "Excellent"
    elif grade >= 50:
        level = "Passable"
    else:
        level = "Bad"
    return level


def show_stars(score):
    stars = "*" * score
    return stars


main()
