class Shape:
    """Base class for all shapes."""
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")


class Circle(Shape):
    """Circle shape with radius."""
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    """Rectangle shape with length and width."""
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):
    """Triangle shape with base and height."""
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
