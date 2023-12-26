# TASK 1 – Set up the donation system
charities = ["Charity A", "Charity B", "Charity C"]
charity_totals = [0, 0, 0]

def display_charities():
    print("Choose a charity:")
    for i, charity in enumerate(charities, start=1):
        print(f"{i}. {charity}")

def get_charity_choice():
    while True:
        try:
            choice = int(input("Enter the number (1, 2, or 3) for your chosen charity: "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_shopping_bill():
    while True:
        try:
            return float(input("Enter the value of your shopping bill: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_donation(bill):
    return bill * 0.01

# TASK 2 – Record and total each donation
def process_donation():
    display_charities()
    choice = get_charity_choice()
    bill = get_shopping_bill()
    donation = calculate_donation(bill)
    charity_totals[choice - 1] += donation
    print(f"Donation of ${donation:.2f} recorded for {charities[choice - 1]}.")

# TASK 3 – Show the totals so far
def show_totals():
    print("\nCharity Totals:")
    sorted_charities = sorted(zip(charities, charity_totals), key=lambda x: x[1], reverse=True)
    grand_total = sum(charity_totals)

    for charity, total in sorted_charities:
        print(f"{charity}: ${total:.2f}")

    print("\nGRAND TOTAL DONATED TO CHARITY:", grand_total)

# Testing
for _ in range(2):  # Simulate donations from two customers
    process_donation()

# Show totals so far
show_totals()
