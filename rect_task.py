import math

# 1. Circle Program
def area(radius: float) -> float:
    """
    Calculates the area of a circle.
    
    Args:
        radius (float): The distance from the center to the edge.
        
    Returns:
        float: The total area of the circle.
    """
    return math.pi * (radius ** 2)
try:
    user_radius = float(input("Enter you radius so i can calculate the area of a circle with your radius: "))
    circle_area = area(user_radius)
    print(f"The area of a circle with a radius of {user_radius}: {circle_area}")
except:
    print("Something went wrong , enter a valid number so i can calculate an area of a circle for you")    

# 2. Rectangle Class
class Rectangle:
    """A class used to represent a Rectangle geometry."""

    def __init__(self, width: float, height:float):
        """Initialises the rectangle with height and width"""
        self.width = width
        self.height = height

    def rect_area(self) -> float:
        """Calculates area by multiplying height by width"""
        return self.height * self.width
    
    def rect_perimeter(self) -> float:
        """Calculates perimeter with height plus width doubled"""
        return 2 * (self.height + self.width)
    
    def is_square(self) -> bool:
        """Checks if the rectangle with given sides is square"""
        return self.height == self.width
    
    def resize(self, new_width: float, new_height: float) -> None:
        """Updates rectangle dimentions.
        
        Args.
            new_width (float) is an updated value of width
            new_height (float) is an updated value of height"""
        self.height = new_height
        self.width = new_width
        print(f"The rectangle is resized to {new_height}x{new_width}")

# 3. Testing
rect = Rectangle(8 , 9)
print(f"Initial dimensions: {rect.width}x{rect.height}")
print(f"The Area: {rect.rect_area()}")

# Fixed the spelling of "square"
print(f"Is it a square? {rect.is_square()}")

rect.resize(8 , 8)
print(f"The new area: {rect.rect_area()}")
print(f"Is it a square now? {rect.is_square()}")