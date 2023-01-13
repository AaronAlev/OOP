"""Shapes."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.__color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.__color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.__color

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.__color = color
        self.__radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return f"Circle (r: {self.__radius}, color: {self.__color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return math.pi * (self.__radius ** 2)


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.__color = color
        self.__side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.__side}, color: {self.__color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.__side ** 2


class Rectangle(Shape):
    """Doc."""

    def __init__(self, color: str, width: float, length: float):
        """Assign values."""
        super().__init__(color)
        self.__width = width
        self.__length = length
        self.__color = color

    def __repr__(self) -> str:
        """Return self."""
        return f"Rectangle (l: {self.__width}, w: {self.__length}, color: {self.__color})"

    def get_area(self) -> float:
        """Calculate area."""
        return self.__width * self.__length


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        total = 0
        for item in self.shapes:
            total += float(item.get_area())
        return total

    def get_circles(self) -> list:
        """Return only circles."""
        circles = []
        for item in self.shapes:
            if isinstance(item, Circle):
                circles.append(item)
        return circles

    def get_squares(self) -> list:
        """Return only squares."""
        squares = []
        for item in self.shapes:
            if isinstance(item, Square):
                squares.append(item)
        return squares

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        rectangles = []
        for item in self.shapes:
            if isinstance(item, Rectangle):
                rectangles.append(item)
        return rectangles


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 3.0)
    square = Square("red", 11.0)
    rectangle = Rectangle("Pink", 3, 5)
    paint.add_shape(circle)
    paint.add_shape(square)
    paint.add_shape(rectangle)
    print(paint.calculate_total_area())
    print(paint.get_circles())
    print(circle.get_area())
    print(square.get_area())
    print(circle.get_color())
    print(rectangle.get_area())
    print(rectangle.get_color())
    print(paint.calculate_total_area())
    print(paint.get_squares())
