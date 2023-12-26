# TASK 1 – Calculate the money taken in a day for one boat
def calculate_daily_profit(boat_number, start_time, end_time):
    hourly_rate = 20
    half_hourly_rate = 12
    total_money_taken = 0
    total_hours_hired = 0

    if start_time < 10 or end_time > 17:
        print("Error: Boats can only be hired between 10:00 and 17:00.")
        return

    duration = end_time - start_time
    if duration >= 1:
        total_money_taken += duration * hourly_rate
        total_hours_hired += duration
    elif 0.5 <= duration < 1:
        total_money_taken += half_hourly_rate
        total_hours_hired += duration

    print(f"Boat {boat_number}: Money taken for the day - ${total_money_taken:.2f}, Total hours hired - {total_hours_hired} hours")

# TASK 2 – Find the next boat available
def find_next_available_boat(current_time):
    available_boats = []
    next_available_time = 17  # Default to end of the day if no boat is available

    for boat_number in range(1, 11):
        if boat_schedule[boat_number]['return_time'] <= current_time:
            available_boats.append(boat_number)
        else:
            next_available_time = min(next_available_time, boat_schedule[boat_number]['return_time'])

    if available_boats:
        print(f"Available boats: {available_boats}")
    else:
        print(f"No boats available. Next available time: {next_available_time}:00")

# TASK 3 – Calculate the money taken for all the boats at the end of the day
def calculate_total_daily_profit():
    total_money_taken = 0
    total_hours_hired = 0
    boats_not_used = []
    boat_most_used = 0
    max_hours_used = 0

    for boat_number in range(1, 11):
        total_money_taken += boat_schedule[boat_number]['money_taken']
        total_hours_hired += boat_schedule[boat_number]['total_hours_hired']

        if boat_schedule[boat_number]['total_hours_hired'] == 0:
            boats_not_used.append(boat_number)

        if boat_schedule[boat_number]['total_hours_hired'] > max_hours_used:
            max_hours_used = boat_schedule[boat_number]['total_hours_hired']
            boat_most_used = boat_number

    print(f"\nTotal money taken for all boats: ${total_money_taken:.2f}")
    print(f"Total hours boats were hired: {total_hours_hired} hours")
    print(f"Boats not used today: {boats_not_used}")
    print(f"Boat {boat_most_used} was used the most with {max_hours_used} hours.")

# Testing
boat_schedule = {i: {'money_taken': 0, 'total_hours_hired': 0, 'return_time': 17} for i in range(1, 11)}

# Simulate hiring for Boat 1 from 10:30 to 12:30
calculate_daily_profit(1, 10.5, 12.5)

# Simulate hiring for Boat 2 from 13:00 to 15:00
calculate_daily_profit(2, 13, 15)

# Simulate checking for available boats at 14:00
find_next_available_boat(14)

# Simulate hiring for Boat 3 from 12:00 to 15:30
calculate_daily_profit(3, 12, 15.5)

# Simulate checking total profits and usage at the end of the day
calculate_total_daily_profit()
