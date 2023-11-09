# Define arrays to store item information
item_codes = ["A1", "A2", "B1", "B2", "B3", "C1", "C2", "C3", "D1", "D2", "E1", "E2", "E3", "F1", "F2", "G1", "G2"]
descriptions = ["A1 Compact", "A2 Tower", "8 GB RAM", "16 GB RAM", "32 GB RAM", "1 TB HDD", "2 TB HDD", "4 TB HDD", "240 GB SSD", "480 GB SSD", "1 TB HDD", "2 TB HDD", "4 TB HDD", "DVD/Blu-Ray Player", "DVD/Blu-Ray Re-writer", "Standard Version OS", "Professional Version OS"]
prices = [75.00, 150.00, 79.99, 149.99, 299.99, 49.99, 89.99, 129.99, 59.99, 119.99, 49.99, 89.99, 129.99, 50.00, 100.00, 100.00, 175.00]

# Initialize variables for the chosen main items
chosen_case = ""
chosen_ram = ""
chosen_hdd = ""
basic_set_cost = 200.00

# Display the available main items
print("Main Items:")
for i in range(2):
    print(f"{item_codes[i]} - {descriptions[i]} - ${prices[i]}")

# Prompt the customer to choose a case
chosen_case = input("Choose a case (A1 or A2): ").strip().upper()
if chosen_case not in ["A1", "A2"]:
    print("Invalid choice for case. Please choose A1 or A2.")
    exit()

# Prompt the customer to choose RAM
for i in range(2, 5):
    print(f"{item_codes[i]} - {descriptions[i]} - ${prices[i]}")
chosen_ram = input("Choose RAM (B1, B2, or B3): ").strip().upper()
if chosen_ram not in ["B1", "B2", "B3"]:
    print("Invalid choice for RAM. Please choose B1, B2, or B3.")
    exit()

# Prompt the customer to choose Main Hard Disk Drive
for i in range(5, 8):
    print(f"{item_codes[i]} - {descriptions[i]} - ${prices[i]}")
chosen_hdd = input("Choose Main Hard Disk Drive (C1, C2, or C3): ").strip().upper()
if chosen_hdd not in ["C1", "C2", "C3"]:
    print("Invalid choice for Main Hard Disk Drive. Please choose C1, C2, or C3.")
    exit()

# Calculate the price of the computer
total_price = basic_set_cost + prices[item_codes.index(chosen_case)] + prices[item_codes.index(chosen_ram)] + prices[item_codes.index(chosen_hdd)]

# Output the chosen items and the total price
print("Chosen Items:")
print(f"Case: {chosen_case} - {descriptions[item_codes.index(chosen_case)]} - ${prices[item_codes.index(chosen_case)]}")
print(f"RAM: {chosen_ram} - {descriptions[item_codes.index(chosen_ram)]} - ${prices[item_codes.index(chosen_ram)]}")
print(f"Main Hard Disk Drive: {chosen_hdd} - {descriptions[item_codes.index(chosen_hdd)]} - ${prices[item_codes.index(chosen_hdd)]}")
print(f"Total Price: ${total_price:.2f}")


#task2



# Initialize variables for additional items
additional_items = []
additional_items_cost = 0.00

# Display available additional items
print("Additional Items:")
for i in range(8, len(item_codes)):
    print(f"{item_codes[i]} - {descriptions[i]} - ${prices[i]}")

# Prompt the customer to choose additional items
while True:
    choice = input("Choose an additional item (or 'done' to finish): ").strip().upper()
    if choice == "DONE":
        break
    if choice in item_codes[8:]:
        additional_items.append(choice)
        additional_items_cost += prices[item_codes.index(choice)]
    else:
        print("Invalid item code. Please choose from the list.")

# Update the total price with additional items cost
total_price += additional_items_cost

# Output the chosen additional items and the updated total price
print("Chosen Additional Items:")
for item in additional_items:
    print(f"{item} - {descriptions[item_codes.index(item)]} - ${prices[item_codes.index(item)]}")
print(f"Updated Total Price: ${total_price:.2f}")


#task3


# Calculate the discount based on the number of additional items
if len(additional_items) == 1:
    discount = 0.05 * total_price
elif len(additional_items) >= 2:
    discount = 0.10 * total_price
else:
    discount = 0.00

# Calculate the final price after applying the discount
final_price = total_price - discount

# Output the discount amount and the final price
print(f"Discount Applied: ${discount:.2f}")
print(f"Final Price after Discount: ${final_price:.2f}")
