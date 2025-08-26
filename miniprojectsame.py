menu = {
    "Tea": 10,
    "Coffee": 20, 
    "Pizza": 40,
    "Barger": 70,
    "Magi": 50,
    "Salad": 35,
    "Mango Shake":40,
    "Orange Juice":30,
    "Papaya Juice":35,
    "Banana Shake":30,
    "Cold Drink":25,
    "Lassi":30,
    "Butter Milk":20
}

print("Welcome to Our Restaurant")

print("---------------MENU----------------")
print("Tea: Rs 10\nCoffee: Rs 20\nPizza: Rs 40\nBarger: Rs 70\nMagi: Rs 50\nSalad: Rs 35\nMango Shake:Rs 40\nOrange Juice: Rs 30 \nPapaya Juice : Rs 35\nBanana Shake: Rs 30\nCold Drink: Rs 25\nLassi:Rs 30\nButter Milk:Rs 20")

total_amount = 0

while True:
    item = input("Enter the name of item which you want to order: ").title()
    if item in menu:
        try: 
           qty=int(input("How many {item} do you want = "))
           total_amount += menu[item]*qty
        except ValueError:
            print("Please enter valid number")

        if total_amount>=100:
            discount=total_amount*0.10    #10% discount
            total_amount-=discount

        print(f"Your item '{item}' has been added to your order.")

    else:
        print(f"Ordered item '{item}' is not available.")

    more = input("Do you want to choose more items (Yes/No)? = ").lower()
    if more != "yes":
        break

print(f"\nYou will have to pay the total amount = Rs{total_amount}")