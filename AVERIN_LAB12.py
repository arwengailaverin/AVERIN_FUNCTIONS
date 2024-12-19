menu = {
    1: ("Filet Mignon", 5000.00),
    2: ("T-Bone Steak", 3500.00),
    3: ("Organic Tenderloin Steak(240g)", 7500.00),
    4: ("Hot Roast Beef", 350.00),
    5: ("Ceasar Salad", 200.00),
    6: ("Truffle Pasta", 550.00),
    7: ("Pasta Cipolla", 400.00),
    8: ("Dry Aged Porterhouse Steak(1kg)", 4700.00)
}

def display_menu():
    print("\nWelcome to the Food Ordering System!")
    print("--- Our Dinner Menu ---")
    for key in menu:
        item, price = menu[key]
        print(f"{key}. {item} - PHP {price}")

def take_order():
    while True:
        try:
            choice = int(input("\nEnter the number of the item you'd like to order: "))
            if choice in menu:
                item, price = menu[choice]
                print(f"You selected {item} which costs PHP {price}")
                return price
            else:
                print("Invalid choice. Please select a valid number from the menu.")
        except ValueError:
            print("Please enter a valid number.")

def process_payment(total):
    while True:
        try:
            cash = float(input(f"\nTotal cost: PHP {total}. Enter cash: PHP "))
            if cash < total:
                print("Not enough cash. Please give more money.")
            else:
                change = cash - total
                print(f"Payment successful. Your change is PHP {change:.2f}")
                return
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

def main():
    display_menu()
    total_cost = take_order()
    process_payment(total_cost)

if __name__ == "__main__":
    main()
