"""
import random

function main():
    get score
    level = choose_score_level(score)
    display(level)

    computer_score = random.randint(0, 100)
    level = choose_score_level(computer_score)
    display(level)

function choose_score_level(grade):
        if grade < 0:
        level = "Invalid score"
        return level
    else:
        if grade > 100:
            level = "Invalid score"
        elif grade > 90:
            level = "Excellent"
        elif grade >= 50:
            level = "Passable"
        else:
            level = "Bad"
        return level
"""
import random


def main():
    score = int(input("Enter score:"))
    level = choose_score_level(score)
    print(level)

    computer_score = random.randint(0, 100)
    level = choose_score_level(computer_score)
    print(level)


def choose_score_level(grade):
    if grade < 0:
        level = "Invalid score"
        return level
    else:
        if grade > 100:
            level = "Invalid score"
        elif grade > 90:
            level = "Excellent"
        elif grade >= 50:
            level = "Passable"
        else:
            level = "Bad"
        return level


main()
