import math

class Hexagon:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcArea(self):
        return (3 * math.sqrt(3) * self.side_length**2) / 2

    def calcPeri(self):
        return 6 * self.side_length

    def calcAngleSum(self):
        return 720  # Sum of angles in a hexagon is always 720 degrees

    def display(self):
        print("Hexagon:")
        print("Area:", self.calcArea())
        print("Perimeter:", self.calcPeri())
        print("Sum of Angles:", self.calcAngleSum())
        print()

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calcAreaSquare(self):
        return self.side_length**2

    def calcPeriSquare(self):
        return 4 * self.side_length

    def displaySquare(self):
        print("Square:")
        print("Area:", self.calcAreaSquare())
        print("Perimeter:", self.calcPeriSquare())
        print()

def main():
    while True:
        print("1. Hexagon")
        print("2. Square")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            side_length = float(input("Enter the side length of the hexagon: "))
            hexagon = Hexagon(side_length)
            hexagon.display()
        elif choice == 2:
            side_length = float(input("Enter the side length of the square: "))
            square = Square(side_length)
            square.displaySquare()
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
