"""Unit conversion handling"""

from ..utils.constants import UNIT_SYSTEMS

class UnitManager:
    """Manages unit systems and conversions"""
    
    def __init__(self):
        self.current_system = "metric"
    
    def set_system(self, system):
        """Set current unit system"""
        if system in UNIT_SYSTEMS:
            self.current_system = system
            return True
        return False
    
    def get_unit(self, measurement_type):
        """Get unit symbol for current system"""
        return UNIT_SYSTEMS[self.current_system].get(measurement_type, '')
    
    def get_length_unit(self):
        """Get length unit for current system"""
        return self.get_unit('length')
    
    def get_area_unit(self):
        """Get area unit for current system"""
        return self.get_unit('area')