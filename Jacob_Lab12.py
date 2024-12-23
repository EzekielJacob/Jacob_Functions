# Simple Food Ordering System

def display_menu(menu):
    print("\nMenu:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def get_order(menu):
    while True:
        choice = input("\nEnter the name of the item you want to order: ").strip()
        if choice in menu:
            return choice, menu[choice]
        else:
            print("Invalid choice. Please select an item from the menu.")

def process_payment(total_cost):
    while True:
        try:
            cash = float(input(f"\nYour total is ${total_cost:.2f}. Enter the amount of cash provided: "))
            if cash >= total_cost:
                return cash
            else:
                print(f"Insufficient payment. You still owe ${total_cost - cash:.2f}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

def calculate_change(cash, total_cost):
    return cash - total_cost

def main():
    # Menu items
    menu = {
        "Burger": 5.99,
        "Pizza": 8.99,
        "Salad": 4.99,
        "Fries": 2.99,
        "Soda": 1.99
    }

    # Display the menu
    display_menu(menu)

    # Get the user's order
    item, price = get_order(menu)
    print(f"\nYou selected: {item} - ${price:.2f}")

    # Process payment
    cash = process_payment(price)

    # Calculate and display change
    change = calculate_change(cash, price)
    print(f"\nPayment successful! Your change is ${change:.2f}. Enjoy your {item}!")

if __name__ == "__main__":
    main()
