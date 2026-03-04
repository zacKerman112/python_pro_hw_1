import math


def calculate_circle_area(radius: float) -> float:
    return math.pi * (radius ** 2)


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.height * self.width

    def get_perimeter(self) -> float:
        return 2 * (self.height + self.width)

    def is_square(self) -> bool:
        return self.height == self.width

    def resize(self, new_width: float, new_height: float) -> None:
        self.height = new_height
        self.width = new_width
        print(f"Resized to: {new_height}x{new_width}")


if __name__ == "__main__":
    try:
        user_radius = float(input("Enter radius: "))
        print(f"Circle area: {calculate_circle_area(user_radius)}")
    except ValueError:
        print("Error: Invalid number")

    print("-" * 20)

    rect = Rectangle(8, 9)
    print(f"Rect: {rect.width}x{rect.height}, Area: {rect.get_area()}")
    
    rect.resize(10, 10)
    print(f"New Area: {rect.get_area()}")
    print(f"Is square: {rect.is_square()}")