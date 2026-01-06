import time

print("Welcome to Moises Vending Machine!")
time.sleep(2)


items = {
    "A1": {"name": "Coke", "price": 3.00, "stock": 10},
    "A2": {"name": "Mountain Dew", "price": 3.50, "stock": 8},
    "A3": {"name": "Royal", "price": 3.25, "stock": 5},
    "B1": {"name": "Snickers", "price": 6.95, "stock": 6},
    "B2": {"name": "Nova Chips", "price": 7.49, "stock": 4},
    "B3": {"name": "Prime", "price": 12.00, "stock": 7},
    "C1": {"name": "San Miguel", "price": 20.00, "stock": 5},
    "C2": {"name": "Bread", "price": 5.00, "stock": 10},
    "C3": {"name": "Mentos", "price": 8.95, "stock": 3}
}

def show_items():
    print("\n--------------------MENU---------------------")
    for code, item in items.items():
        print(f"{code}: {item['name']} - ${item['price']} (Stock: {item['stock']})")
    print("-----------------------------------------------")

def pay(total):
    while True:
        method = input("Do you want to pay by Card or Cash? ").strip().lower()
        if method == "card":
            print(f"Processing card payment of ${total:.2f}...")
            time.sleep(1)
            print("Payment successful!")
            return True
        elif method == "cash":
            while True:
                try:
                    cash = float(input(f"Insert cash (total ${total:.2f}): "))
                    if cash < total:
                        print(f"Not enough. You need ${total - cash:.2f} more.")
                    else:
                        change = cash - total
                        print("Payment successful!")
                        if change > 0:
                            print(f"Here is your change: ${change:.2f}")
                        return True
                except ValueError:
                    print("Please enter a valid number.")
        else:
            print("Invalid choice. Please type 'Card' or 'Cash'.")

def order():
    cart = []
    total = 0

    show_items()
    while True:
        code = input("Select an item code like (A1) or type 'Done' to cancel: ").strip().capitalize()
        if code == "Done":
            break
        if code not in items:
            print("Invalid code. Please select a correct code.")
            continue
        if items[code]["stock"] <= 0:
            print("Sorry, the item you selected is out of stock.")
            continue

        quantity = input(f"How many {items[code]['name']} would you like? ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Enter a valid number.")
            continue
        quantity = int(quantity)
        if quantity > items[code]["stock"]:
            quantity = items[code]["stock"]
            print(f"Only {quantity} available. Quantity adjusted.")

        cart.append({
            "code": code,
            "name": items[code]["name"],
            "price": items[code]["price"],
            "quantity": quantity
        })
        total += items[code]["price"] * quantity
        print(f"Added {quantity} x {items[code]['name']} - Current total: ${total:.2f}")

       
        more = input("Do you want to add more items? (yes/no): ").strip().lower()
        if more != "yes":
            break 

    if not cart:
        print("No items selected.")
        return

    print(f"\nTotal to pay: ${total:.2f}")
    if pay(total):
        print("\n--- Receipt ---")
        for item in cart:
            print(f"{item['quantity']} x {item['name']} - ${item['price']*item['quantity']:.2f}")
            items[item['code']]["stock"] -= item["quantity"]
        print("Payment completed.")
        print("Thank you for shopping!\n")

    
    else:
        print("Thank you for purchasing in Moises Vending Machine and have a nice day ahead! Don't Forget to smile always")


order()