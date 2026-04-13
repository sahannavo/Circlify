"""Input validation with human-centered error messages"""

class Validator:
    """Handles all input validation with friendly messages"""
    
    @staticmethod
    def validate_radius(value):
        """
        Validate radius input
        
        Returns:
            tuple: (is_valid, error_message, float_value)
        """
        # Check for empty input
        if not value or value.strip() == "":
            return False, "✨ Please enter a radius value to begin", None
        
        # Check if it's a valid number
        try:
            radius = float(value)
        except ValueError:
            return False, "🔢 Please enter a valid number (e.g., 5, 2.5, 10.75)", None
        
        # Check for negative
        if radius < 0:
            return False, "💡 Radius cannot be negative. Please enter a positive number.", None
        
        # Special case: zero
        if radius == 0:
            return True, "📐 Radius is zero. The circle would be a point.", 0.0
        
        return True, None, radius
    
    @staticmethod
    def validate_calculation_type(calc_type):
        """Validate that a calculation type is selected"""
        if not calc_type:
            return False, "🎯 Please select what you'd like to calculate"
        return True, None