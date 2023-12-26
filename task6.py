# TASK 1 – Check the contents and weight of a single sack
def check_single_sack():
    contents = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ").upper()

    if contents not in {'C', 'G', 'S'}:
        print("Rejected: Invalid contents. Please enter C, G, or S.")
        return False

    weight = float(input("Enter the weight of the sack in kilograms: "))

    if (contents in {'G', 'S'} and 49.9 < weight < 50.1) or (contents == 'C' and 24.9 < weight < 25.1):
        print(f"Accepted: Sack contains {contents} and weighs {weight} kilograms.")
        return True
    else:
        print("Rejected: Invalid weight or contents.")
        return False

# TASK 2 – Check a customer’s order for delivery
def check_customer_order():
    total_weight = 0
    sacks_rejected = 0

    num_cement = int(input("Enter the number of cement sacks required: "))
    num_gravel = int(input("Enter the number of gravel sacks required: "))
    num_sand = int(input("Enter the number of sand sacks required: "))

    for _ in range(num_cement):
        if not check_single_sack():
            sacks_rejected += 1
        else:
            total_weight += 25

    for _ in range(num_gravel):
        if not check_single_sack():
            sacks_rejected += 1
        else:
            total_weight += 50

    for _ in range(num_sand):
        if not check_single_sack():
            sacks_rejected += 1
        else:
            total_weight += 50

    print(f"\nTotal weight of the order: {total_weight} kilograms")
    print(f"Number of sacks rejected from the order: {sacks_rejected}")

# TASK 3 – Calculate the price for a customer’s order
def calculate_order_price():
    regular_price = 3 * (num_cement + num_gravel + num_sand)

    num_special_packs = min(num_cement, num_sand // 2, num_gravel // 2)
    discount_price = 10 * num_special_packs
    amount_saved = regular_price - discount_price

    print(f"\nRegular price for the order: ${regular_price}")
    if num_special_packs > 0:
        print(f"Discount price for special packs: ${discount_price}")
        print(f"New price for the order: ${regular_price - amount_saved} (You saved ${amount_saved})")
    else:
        print("No special packs in the order.")

# Testing
check_customer_order()
calculate_order_price()
