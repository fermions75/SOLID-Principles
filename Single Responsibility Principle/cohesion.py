# Cohesion is a measure of how related and focused the responsibilities of a module are. A module with high cohesion is focused on a single task or a group of related tasks.

class Square:

    def __init__(self) -> None:
        self.side:int = 5
    
    def calculate_area(self) -> int:
        return self.side * self.side
    
    def calculate_perimeter(self) -> int:
        return 4 * self.side
    
    def draw(self):
        # draw a circle in the UI
        pass

    def rotate(self):
        # rotate the circle
        pass

"""
Here, the first 2 methods are highly cohesive since they perform similar type of responsibility. But method 3 and 4 are not related to the first 2 methods.
This class violates the Single responsibility principle. To maintain high cohesion in modules, we can rewrite the class in the following way -
"""

# Responsible for calculating the area and perimeter of a square
class Square:
    def __init__(self) -> None:
        self.side:int = 5
    
    def calculate_area(self) -> int:
        return self.side * self.side
    
    def calculate_perimeter(self) -> int:
        return 4 * self.side
    

# Responsible for drawing and rotating the square
class SquareUI:

    def draw(self):
        # draw a circle in the UI
        pass

    def rotate(self, degree:int):
        # rotate the circle and return the rotated circle
        pass


"""
Now, the class Square has high cohesion and the class SquareUI has high cohesion. Both classes are now following the Single Responsibility Principle.
"""