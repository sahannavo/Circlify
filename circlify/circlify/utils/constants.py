"""Constants used throughout Circlify"""

import math

# Mathematical constants
PI = math.pi

# UI constants
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 650
CORNER_RADIUS = 30

# Color palette (modern, human-centered)
COLORS = {
    'bg': '#f5f7fa',           # Soft off-white
    'card': '#ffffff',          # Pure white
    'primary': '#6366f1',       # Indigo (calming)
    'primary_hover': '#4f46e5', # Darker indigo
    'secondary': '#10b981',     # Emerald green
    'danger': '#ef4444',        # Soft red
    'text': '#1f2937',          # Dark gray
    'text_light': '#6b7280',    # Medium gray
    'border': '#e5e7eb'         # Light gray
}

# Unit systems
UNIT_SYSTEMS = {
    'metric': {
        'length': 'cm',
        'area': 'cm²'
    },
    'imperial': {
        'length': 'in',
        'area': 'in²'
    }
}

# Calculation types
CALC_TYPES = {
    'diameter': {
        'name': 'Diameter',
        'formula': '2 × radius',
        'icon': '○'
    },
    'circumference': {
        'name': 'Circumference', 
        'formula': '2πr',
        'icon': '◯'
    },
    'area': {
        'name': 'Area',
        'formula': 'πr²',
        'icon': '●'
    }
}