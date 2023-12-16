"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

Pseudocode
get sales
while sales >= 0
    if sales >= 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    get sales
"""

SALES_THRESHOLD = 1000
LOWEST_SALES = 0
FIRST_LEVEL_BONUS = 0.1
SECOND_LEVEL_BONUS = 0.15

sales = float(input("Enter sales: $ "))
while sales >= LOWEST_SALES:
    if sales < SALES_THRESHOLD:
        bonus = sales * FIRST_LEVEL_BONUS
    else:
        bonus = sales * SECOND_LEVEL_BONUS
    print(f"Sales are ${sales}, the bonus is ${bonus:.2f}")
    sales = float(input("Enter sales: $ "))
