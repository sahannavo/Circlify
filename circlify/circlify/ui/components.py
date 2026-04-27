"""Reusable UI components"""

import tkinter as tk
from tkinter import ttk
from ..utils.constants import COLORS

class ModernCard(tk.Frame):
    """Modern card component with rounded corners"""
    
    def __init__(self, parent, title, **kwargs):
        super().__init__(parent, bg=COLORS['card'], **kwargs)
        self.title = title
        self.setup_ui()
    
    def setup_ui(self):
        # Subtle border
        border = tk.Frame(self, bg=COLORS['border'], height=1)
        border.pack(fill=tk.X, padx=15, pady=(15, 0))
        
        # Title
        title_label = tk.Label(
            self, text=self.title,
            font=('Segoe UI', 12, 'bold'),
            bg=COLORS['card'], fg=COLORS['primary']
        )
        title_label.pack(anchor='w', pady=(15, 10), padx=15)
        
        # Content frame (to be used by parent)
        self.content = tk.Frame(self, bg=COLORS['card'])
        self.content.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 15))

class SegmentedControl(tk.Frame):
    """Modern segmented control for unit selection"""
    
    def __init__(self, parent, options, variable, **kwargs):
        super().__init__(parent, bg=COLORS['card'], **kwargs)
        self.options = options
        self.variable = variable
        self.buttons = []
        self.setup_ui()
    
    def setup_ui(self):
        for i, (text, value) in enumerate(self.options.items()):
            btn = tk.Button(
                self, text=text,
                font=('Segoe UI', 10),
                bg=COLORS['card'], fg=COLORS['text'],
                relief='flat', bd=1,
                command=lambda v=value: self.select(v)
            )
            btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0 if i==0 else 5, 0))
            self.buttons.append((btn, value))
        
        self.update_style()
        self.variable.trace('w', lambda *args: self.update_style())
    
    def select(self, value):
        self.variable.set(value)
    
    def update_style(self):
        current = self.variable.get()
        for btn, value in self.buttons:
            if current == value:
                btn.configure(bg=COLORS['primary'], fg='white')
            else:
                btn.configure(bg=COLORS['card'], fg=COLORS['text'])