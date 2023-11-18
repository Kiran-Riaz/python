# Define the source data matrix
source_data = [
    [50, 120, 250],
    [150, 180, 300],
    [250, 280, 350]
]

# Function to calculate and display cost for slab 1
def costSlab1():
    unit_range = "0-100"
    cost_per_unit = 10
    slab_data = source_data[0]
    display_cost(unit_range, cost_per_unit, slab_data)

# Function to calculate and display cost for slab 2
def costSlab2():
    unit_range = "101-200"
    cost_per_unit = 15
    slab_data = source_data[1]
    display_cost(unit_range, cost_per_unit, slab_data)

# Function to calculate and display cost for slab 3
def costSlab3():
    unit_range = "201-300"
    cost_per_unit = 20
    slab_data = source_data[2]
    display_cost(unit_range, cost_per_unit, slab_data)

# Function to display the cost for a given slab
def display_cost(unit_range, cost_per_unit, slab_data):
    total_units = sum(slab_data)
    total_cost = total_units * cost_per_unit
    print(f"Unit Range: {unit_range}")
    print(f"Total Units: {total_units}")
    print(f"Cost per Unit: Rs.{cost_per_unit}")
    print(f"Total Cost: Rs.{total_cost}")
    print("\n")

# Main program
student_id = input("Enter student's ID: ")
while True:
    print("1. Display bill of slab 1 and slab 2")
    print("2. Display bill of slab 3")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"\nBill for {student_id}:")
        costSlab1()
        costSlab2()
    elif choice == "2":
        print(f"\nBill for {student_id}:")
        costSlab3()
    elif choice == "3":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.\n")
