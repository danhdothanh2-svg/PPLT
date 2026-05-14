class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def calculate_area(self):
        return self.length * self.width


# Create 2 Rectangle objects
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(7, 3)

print("Rectangle 1")
print("Perimeter:", rectangle1.calculate_perimeter())
print("Area:", rectangle1.calculate_area())

print("Rectangle 2")
print("Perimeter:", rectangle2.calculate_perimeter())
print("Area:", rectangle2.calculate_area())