class ElectricMountainRailway:
    def __init__(self):
        # Initialize data structures
        self.available_tickets = {'up': [80, 80, 80, 80], 'down': [80, 80, 80, 80]}
        self.total_passengers = {'up': [0, 0, 0, 0], 'down': [0, 0, 0, 0]}
        self.total_money = {'up': [0, 0, 0, 0], 'down': [0, 0, 0, 0]}

    def display_train_times(self):
        # Display train times and available tickets
        print("Train Times:")
        for i in range(4):
            print(f"{9 + i * 2}:00 - {10 + i * 2}:00, Available Tickets: {self.available_tickets['up'][i]}")

            if i < 3:
                print(f"{10 + i * 2}:00 - {11 + i * 2}:00, Available Tickets: {self.available_tickets['down'][i]}")
            else:
                print(f"{10 + i * 2}:00 - {11 + i * 2}:00, Available Tickets: {self.available_tickets['down'][i]} (2 extra coaches)")

    def purchase_tickets(self, journey_type, num_passengers):
        # Purchase tickets for a single passenger or a group
        if self.available_tickets[journey_type][0] >= num_passengers:
            # Calculate total price including any group discount
            ticket_price = 25
            total_price = num_passengers * ticket_price

            # Update data structures
            self.available_tickets[journey_type][0] -= num_passengers
            self.total_passengers[journey_type][0] += num_passengers
            self.total_money[journey_type][0] += total_price

            # Update display
            print(f"Tickets purchased for {num_passengers} passengers on the {journey_type} journey.")
            self.display_train_times()
        else:
            print(f"Sorry, not enough tickets available for {num_passengers} passengers on the {journey_type} journey.")

    def end_of_day_report(self):
        # Display end-of-day report
        print("\nEnd-of-Day Report:")
        for i in range(4):
            print(f"Journey {i + 1} (Up): {self.total_passengers['up'][i]} passengers, ${self.total_money['up'][i]}")
            print(f"Journey {i + 1} (Down): {self.total_passengers['down'][i]} passengers, ${self.total_money['down'][i]}")

        total_passengers_day = sum(sum(self.total_passengers.values(), []))
        total_money_day = sum(sum(self.total_money.values(), []))
        print(f"\nTotal Passengers for the Day: {total_passengers_day}")
        print(f"Total Money for the Day: ${total_money_day}")

        # Find and display the journey with the most passengers
        max_passengers_journey = max(self.total_passengers['up'] + self.total_passengers['down'])
        print(f"Journey with the Most Passengers: Journey {max_passengers_journey}")

# Example usage
railway = ElectricMountainRailway()

# Task 1 - Start of the day
railway.display_train_times()

# Task 2 - Purchasing tickets
railway.purchase_tickets('up', 5)
railway.purchase_tickets('down', 10)

# Task 3 - End of the day
railway.end_of_day_report()
