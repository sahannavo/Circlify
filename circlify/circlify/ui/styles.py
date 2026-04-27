"""UI styling and theme management"""

from ..utils.constants import COLORS, CORNER_RADIUS

class CirclifyStyle:
    """Manages all UI styling"""
    
    def __init__(self):
        self.colors = COLORS
        self.corner_radius = CORNER_RADIUS
    
    def apply_button_style(self, button, is_primary=True):
        """Apply modern button styling"""
        if is_primary:
            bg = self.colors['primary']
            fg = 'white'
            hover = self.colors['primary_hover']
        else:
            bg = self.colors['card']
            fg = self.colors['text']
            hover = self.colors['border']
        
        button.configure(
            bg=bg, fg=fg,
            relief='flat', bd=0,
            font=('Segoe UI', 11, 'bold'),
            cursor='hand2',
            activebackground=hover,
            activeforeground='white'
        )
        
        # Add hover effects
        def on_enter(e):
            button.configure(bg=hover)
        
        def on_leave(e):
            button.configure(bg=bg)
        
        button.bind('<Enter>', on_enter)
        button.bind('<Leave>', on_leave)
        
        return button
    
    def get_card_style(self):
        """Return card styling configuration"""
        return {
            'bg': self.colors['card'],
            'relief': 'flat'
        }