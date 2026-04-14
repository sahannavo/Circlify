"""Main Circlify application class"""

import tkinter as tk
from tkinter import ttk

from .utils.constants import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT
from .core.validator import Validator
from .core.calculator import CircleCalculator
from .core.units import UnitManager
from .ui.styles import CirclifyStyle
from .ui.components import ModernCard, SegmentedControl

class CirclifyApp:
    """Main application class - Human-centered circle calculator"""
    
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Circlify")
        self.app.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.app.resizable(False, False)
        self.app.configure(bg=COLORS['bg'])
        
        # Initialize components
        self.calculator = CircleCalculator()
        self.validator = Validator()
        self.units = UnitManager()
        self.style = CirclifyStyle()
        
        # Variables
        self.unit_var = tk.StringVar(value="metric")
        self.calc_var = tk.StringVar()
        
        self.setup_ui()
        self.setup_shortcuts()
        
    def setup_ui(self):
        """Setup the entire user interface"""
        # Main container
        main_frame = tk.Frame(self.app, bg=COLORS['bg'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Hero section
        self.create_hero_section(main_frame)
        
        # Input card
        input_card = ModernCard(main_frame, "📊 Input Values")
        
        # Radius input
        self.create_radius_input(input_card.content)
        
        # Unit selector
        self.create_unit_selector(input_card.content)
        
        # Calculation type card
        calc_card = ModernCard(main_frame, "🧮 Calculation Type")
        self.create_calculation_selector(calc_card.content)
        
        # Action buttons
        self.create_action_buttons(main_frame)
        
        # Result card
        result_card = ModernCard(main_frame, "✨ Result")
        self.result_label = tk.Label(
            result_card.content,
            text="Ready to calculate...",
            font=('Segoe UI', 12),
            bg=COLORS['card'],
            fg=COLORS['text_light'],
            wraplength=350,
            justify=tk.CENTER
        )
        self.result_label.pack(pady=20, padx=20)
        
        # Error display
        self.error_label = tk.Label(
            main_frame, text="",
            font=('Segoe UI', 10),
            bg=COLORS['bg'],
            fg=COLORS['danger']
        )
        self.error_label.pack(pady=(0, 20))
        
        # Quick reference
        self.create_reference_card(main_frame)
    
    def create_hero_section(self, parent):
        """Create welcoming hero section"""
        hero = tk.Frame(parent, bg=COLORS['primary'], height=100)
        hero.pack(fill=tk.X, pady=(0, 20))
        hero.pack_propagate(False)
        
        tk.Label(
            hero, text="🟣",
            font=('Segoe UI', 32),
            bg=COLORS['primary'], fg='white'
        ).pack(pady=(15, 0))
        
        tk.Label(
            hero, text="Circlify",
            font=('Segoe UI', 18, 'bold'),
            bg=COLORS['primary'], fg='white'
        ).pack()
        
        tk.Label(
            hero, text="Simplify Your Circles",
            font=('Segoe UI', 10),
            bg=COLORS['primary'],
            fg='rgba(255,255,255,0.9)'
        ).pack()
    
    def create_radius_input(self, parent):
        """Create radius input field"""
        tk.Label(
            parent, text="Radius",
            font=('Segoe UI', 11, 'bold'),
            bg=COLORS['card'], fg=COLORS['text']
        ).pack(anchor='w')
        
        entry_frame = tk.Frame(parent, bg=COLORS['border'])
        entry_frame.pack(fill=tk.X, pady=(5, 10))
        
        tk.Label(
            entry_frame, text="📏",
            font=('Segoe UI', 14),
            bg='white', fg=COLORS['primary']
        ).pack(side=tk.LEFT, padx=10, pady=10)
        
        self.radius_entry = tk.Entry(
            entry_frame,
            font=('Segoe UI', 13),
            bg='white', fg=COLORS['text'],
            bd=0, highlightthickness=0
        )
        self.radius_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), pady=10)
        entry_frame.configure(bg='white')
    
    def create_unit_selector(self, parent):
        """Create unit selection control"""
        tk.Label(
            parent, text="Unit System",
            font=('Segoe UI', 11, 'bold'),
            bg=COLORS['card'], fg=COLORS['text']
        ).pack(anchor='w')
        
        unit_frame = tk.Frame(parent, bg=COLORS['card'])
        unit_frame.pack(fill=tk.X, pady=(5, 10))
        
        SegmentedControl(
            unit_frame,
            {"Metric (cm)": "metric", "Imperial (in)": "imperial"},
            self.unit_var
        ).pack(fill=tk.X)
    
    def create_calculation_selector(self, parent):
        """Create calculation type radio buttons"""
        calc_types = [
            ("○", "Diameter", "2 × radius", "circle's diameter"),
            ("◯", "Circumference", "2πr", "circle's circumference"),
            ("●", "Area", "πr²", "circle's area")
        ]
        
        for icon, name, formula, value in calc_types:
            radio_frame = tk.Frame(parent, bg=COLORS['card'])
            radio_frame.pack(fill=tk.X, pady=8)
            
            rb = tk.Radiobutton(
                radio_frame, text=f"{icon}  {name}",
                variable=self.calc_var, value=value,
                bg=COLORS['card'], fg=COLORS['text'],
                font=('Segoe UI', 11, 'bold'),
                selectcolor=COLORS['card'],
                activebackground=COLORS['card'],
                relief='flat', highlightthickness=0
            )
            rb.pack(side=tk.LEFT)
            
            formula_label = tk.Label(
                radio_frame, text=formula,
                bg=COLORS['card'], fg=COLORS['text_light'],
                font=('Segoe UI', 9, 'italic')
            )
            formula_label.pack(side=tk.RIGHT)
    
    def create_action_buttons(self, parent):
        """Create calculate and clear buttons"""
        button_frame = tk.Frame(parent, bg=COLORS['bg'])
        button_frame.pack(fill=tk.X, pady=10)
        
        calc_btn = tk.Button(
            button_frame, text="Calculate",
            command=self.calculate,
            font=('Segoe UI', 11, 'bold'),
            padx=20, pady=10
        )
        calc_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        self.style.apply_button_style(calc_btn, is_primary=True)
        
        clear_btn = tk.Button(
            button_frame, text="Clear All",
            command=self.clear_all,
            font=('Segoe UI', 11, 'bold'),
            padx=20, pady=10
        )
        clear_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))
        self.style.apply_button_style(clear_btn, is_primary=False)
    
    def create_reference_card(self, parent):
        """Create quick reference card"""
        ref_card = ModernCard(parent, "📖 Quick Reference")
        ref_text = """• Diameter = 2 × radius
• Circumference = 2πr (π ≈ 3.14159)
• Area = πr²

💡 Tip: Press 'Enter' to calculate quickly!"""
        
        tk.Label(
            ref_card.content, text=ref_text,
            font=('Segoe UI', 10),
            bg=COLORS['card'], fg=COLORS['text_light'],
            justify=tk.LEFT
        ).pack(pady=10, padx=15, anchor='w')
    
    def setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        self.app.bind('<Return>', lambda event: self.calculate())
        self.app.bind('<Escape>', lambda event: self.clear_all())
    
    def calculate(self):
        """Perform calculation with validation"""
        self.error_label.config(text="")
        
        # Validate radius
        radius_text = self.radius_entry.get()
        is_valid, error_msg, radius = self.validator.validate_radius(radius_text)
        
        if not is_valid:
            self.error_label.config(text=error_msg)
            self.result_label.config(text="Invalid input", fg=COLORS['danger'])
            return
        
        if error_msg:  # Warning message (like radius = 0)
            self.error_label.config(text=error_msg)
        
        # Validate calculation type
        calc_type = self.calc_var.get()
        is_valid, error_msg = self.validator.validate_calculation_type(calc_type)
        
        if not is_valid:
            self.error_label.config(text=error_msg)
            self.result_label.config(text="Selection required", fg=COLORS['text_light'])
            return
        
        # Perform calculation
        result, formula = self.calculator.calculate(radius, calc_type)
        
        # Format result
        result_str = self.calculator.format_result(result)
        
        # Get unit
        if calc_type == "circle's area":
            unit = self.units.get_area_unit()
        else:
            unit = self.units.get_length_unit()
        
        # Get calculation name
        calc_names = {
            "circle's diameter": "Diameter",
            "circle's circumference": "Circumference",
            "circle's area": "Area"
        }
        
        # Create result message
        result_text = f"""🎉 {calc_names[calc_type]}: {result_str} {unit}

📐 Radius: {radius} {self.units.get_length_unit()}
📝 Formula: {formula}
✨ π = 3.14159"""
        
        self.result_label.config(text=result_text, fg=COLORS['text'])
        self.error_label.config(text="✅ Calculation complete!")
        
        # Clear success message after 2 seconds
        self.app.after(2000, lambda: self.clear_success_message())
    
    def clear_success_message(self):
        """Clear success message after delay"""
        if self.error_label.cget("text") == "✅ Calculation complete!":
            self.error_label.config(text="")
    
    def clear_all(self):
        """Clear all inputs"""
        self.radius_entry.delete(0, tk.END)
        self.calc_var.set("")
        self.result_label.config(text="Ready to calculate...", fg=COLORS['text_light'])
        self.error_label.config(text="✨ All cleared! Ready for new calculation")
        self.radius_entry.focus_set()
        
        # Clear message after 2 seconds
        self.app.after(2000, lambda: self.clear_success_message())
    
    def run(self):
        """Run the application"""
        # Center window on screen
        self.app.update_idletasks()
        x = (self.app.winfo_screenwidth() // 2) - (WINDOW_WIDTH // 2)
        y = (self.app.winfo_screenheight() // 2) - (WINDOW_HEIGHT // 2)
        self.app.geometry(f'+{x}+{y}')
        
        self.app.mainloop()