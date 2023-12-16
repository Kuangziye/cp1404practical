"""
total_price = 0
DISCOUNT_THRESHOLD = 100

get number_of_items
while number_of_items < 0:
    display Invalid number of items!
    get Invalid number of items!

for i in range(0, number_of_items):
    get price
    total_price += price
if total_price <= DISCOUNT_THRESHOLD:
    discount_price = total_price
else:
    discount_price = total_price * 0.9
display discount_price

"""
total_price = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT = 0.9

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(0, number_of_items):
    price = float(input("Price of item: "))
    total_price += price
if total_price <= DISCOUNT_THRESHOLD:
    discount_price = total_price
else:
    discount_price = total_price * DISCOUNT
print(f"Total price for 3 items is ${discount_price:.2f}")
