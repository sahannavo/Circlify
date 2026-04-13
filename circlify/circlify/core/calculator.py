"""Core calculation logic"""

from ..utils.constants import PI

class CircleCalculator:
    """Handles all circle calculations"""
    
    @staticmethod
    def calculate_diameter(radius):
        """Calculate diameter = 2 × radius"""
        return 2 * radius
    
    @staticmethod
    def calculate_circumference(radius):
        """Calculate circumference = 2πr"""
        return 2 * PI * radius
    
    @staticmethod
    def calculate_area(radius):
        """Calculate area = πr²"""
        return PI * (radius ** 2)
    
    @staticmethod
    def format_result(value):
        """Format result based on magnitude (human-centered)"""
        if value < 0.01:
            return f"{value:.6f}"
        elif value < 1:
            return f"{value:.4f}"
        elif value < 1000:
            return f"{value:.2f}"
        else:
            return f"{value:.1f}"
    
    def calculate(self, radius, calc_type):
        """Main calculation dispatcher"""
        if calc_type == "circle's diameter":
            result = self.calculate_diameter(radius)
            formula = "Diameter = 2 × radius"
        elif calc_type == "circle's circumference":
            result = self.calculate_circumference(radius)
            formula = "Circumference = 2πr"
        else:  # area
            result = self.calculate_area(radius)
            formula = "Area = πr²"
        
        return result, formula