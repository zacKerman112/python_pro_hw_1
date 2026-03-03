import math


def area(radius):
    return math.pi * (radius**2)
try:
    user_radius = float(input("Enter you radius so i can calculate the area of a circle with your radius: "))
    area = area(user_radius)
    print(f"The area of a circle with a radius of {user_radius}: {area}")
except:
    print("Something went wrong , enter a valid number so i can calculate an area of a circle for you")    


class Rectangle:


    def __init__(self, width, height):
        self.width = width
        self.height = height


    def rect_area(self):
        return self.height * self.width
    

    def rect_perimeter(self):
        return 2 * (self.height + self.width)
    

    def is_sqare(self):
        return self.height == self.width
    

    def resize(self, new_width, new_height):
        self.height = new_height
        self.width = new_width
        print(f"The rectangle is resized to {new_height}x{new_width}")


rect = Rectangle(8 , 9)
print(f"Initial dimensions: {rect.width}x{rect.height}")
print(f"The Area: {rect.rect_area()}")

print(f"Is it a square? {rect.is_sqare()}")

rect.resize(8 , 8)
print(f"The new area: {rect.rect_area()}")
print(f"Is it a square now? {rect.is_sqare()}")