"""Main Circlify application class"""

import tkinter as tk
from tkinter import ttk
import math

class CirclifyApp:
    """Main application class - Human-centered circle calculator"""
    
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Circlify")
        
        self.app.geometry("550x750")
        self.app.minsize(500, 650)
        self.app.maxsize(700, 750)
        self.app.resizable(True, True)
        
        self.colors = {
            'bg': '#f5f7fa',
            'card': '#ffffff',
            'primary': '#6366f1',
            'primary_hover': '#4f46e5',
            'secondary': '#10b981',
            'danger': '#ef4444',
            'text': '#1f2937',
            'text_light': '#6b7280',
            'border': '#e5e7eb',
            'input_bg': '#f9fafb'
        }
        
        self.app.configure(bg=self.colors['bg'])
        
        self.main_container = tk.Frame(self.app, bg=self.colors['bg'])
        self.main_container.pack(fill=tk.BOTH, expand=True)
        
        self.create_header()
        self.create_scrollable_area()
        self.create_ui()
        self.setup_shortcuts()
        
    def create_header(self):
        """Create header with window controls"""
        header_frame = tk.Frame(self.main_container, bg=self.colors['primary'], height=60)
        header_frame.pack(fill=tk.X, side=tk.TOP)
        header_frame.pack_propagate(False)
        
        title = tk.Label(header_frame, text="○ Circle Calculator", 
                        bg=self.colors['primary'], fg='white',
                        font=('Segoe UI', 16, 'bold'))
        title.pack(side=tk.LEFT, padx=20, pady=15)
        
        close_btn = tk.Button(header_frame, text='✕', 
                             bg=self.colors['primary'], fg='white',
                             bd=0, font=('Segoe UI', 18, 'bold'),
                             activebackground=self.colors['primary_hover'],
                             activeforeground='white',
                             command=self.app.destroy,
                             cursor='hand2')
        close_btn.pack(side=tk.RIGHT, padx=15, pady=12)
        
        min_btn = tk.Button(header_frame, text='−', 
                           bg=self.colors['primary'], fg='white',
                           bd=0, font=('Segoe UI', 22, 'bold'),
                           activebackground=self.colors['primary_hover'],
                           activeforeground='white',
                           command=self.minimize_window,
                           cursor='hand2')
        min_btn.pack(side=tk.RIGHT, padx=5, pady=12)
        
    def create_scrollable_area(self):
        """Create scrollable area for content"""
        self.canvas = tk.Canvas(self.main_container, bg=self.colors['bg'],
                                highlightthickness=0)
        self.scrollbar = ttk.Scrollbar(self.main_container, orient="vertical", 
                                       command=self.canvas.yview)
        
        self.scrollable_frame = tk.Frame(self.canvas, bg=self.colors['bg'])
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")))
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, 
                                                       anchor="nw")
        
        def configure_canvas(event):
            self.canvas.itemconfig(self.canvas_window, width=event.width)
        
        self.canvas.bind('<Configure>', configure_canvas)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        
        def on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
        self.canvas.bind_all("<MouseWheel>", on_mousewheel)
        
    def minimize_window(self):
        """Minimize the window"""
        self.app.iconify()
        
    def create_card(self, parent, title):
        """Create a modern card with title"""
        card = tk.Frame(parent, bg=self.colors['card'], relief=tk.FLAT)
        card.pack(fill=tk.X, pady=10, padx=20)
        
        header_border = tk.Frame(card, bg=self.colors['border'], height=1)
        header_border.pack(fill=tk.X, padx=20, pady=(20, 0))
        
        title_label = tk.Label(card, text=title,
                              font=('Segoe UI', 13, 'bold'),
                              bg=self.colors['card'], fg=self.colors['primary'])
        title_label.pack(anchor='w', padx=20, pady=(15, 15))
        
        content = tk.Frame(card, bg=self.colors['card'])
        content.pack(fill=tk.X, padx=20, pady=(0, 20))
        
        return content
        
    def create_ui(self):
        """Create all UI components"""
        
        # Hero section
        hero = tk.Frame(self.scrollable_frame, bg=self.colors['primary'], height=120)
        hero.pack(fill=tk.X, pady=(0, 20))
        hero.pack_propagate(False)
        
        tk.Label(hero, text="🔵", font=('Segoe UI', 36),
                bg=self.colors['primary'], fg='white').pack(pady=(15, 5))
        
        tk.Label(hero, text="Circle Calculator", font=('Segoe UI', 20, 'bold'),
                bg=self.colors['primary'], fg='white').pack()
        
        tk.Label(hero, text="Quick & accurate circle calculations", 
                font=('Segoe UI', 11), bg=self.colors['primary'], 
                fg='#E6E6E6').pack(pady=(5, 15))
        
        # Input Values Card
        input_card = self.create_card(self.scrollable_frame, "📊 Input Values")
        
        # Radius input
        radius_label = tk.Label(input_card, text="Radius", 
                               font=('Segoe UI', 12, 'bold'),
                               bg=self.colors['card'], fg=self.colors['text'])
        radius_label.pack(anchor='w', pady=(0, 5))
        
        entry_frame = tk.Frame(input_card, bg=self.colors['border'], 
                              highlightthickness=0, bd=1, relief=tk.FLAT)
        entry_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.radius_entry = tk.Entry(entry_frame, font=('Segoe UI', 13),
                                     bg=self.colors['input_bg'], 
                                     fg=self.colors['text'],
                                     bd=0, highlightthickness=0)
        self.radius_entry.pack(fill=tk.X, padx=2, pady=2, ipady=8)
        
        # Unit System
        unit_label = tk.Label(input_card, text="Unit System", 
                             font=('Segoe UI', 12, 'bold'),
                             bg=self.colors['card'], fg=self.colors['text'])
        unit_label.pack(anchor='w', pady=(10, 5))
        
        self.unit_var = tk.StringVar(value="metric")
        
        unit_frame = tk.Frame(input_card, bg=self.colors['card'])
        unit_frame.pack(fill=tk.X, pady=(0, 5))
        
        metric_rb = tk.Radiobutton(unit_frame, text="Metric (cm/m)", 
                                   variable=self.unit_var, value="metric",
                                   bg=self.colors['card'], fg=self.colors['text'],
                                   font=('Segoe UI', 11),
                                   selectcolor=self.colors['card'],
                                   activebackground=self.colors['card'],
                                   cursor='hand2')
        metric_rb.pack(anchor='w', pady=5)
        
        imperial_rb = tk.Radiobutton(unit_frame, text="Imperial (in/ft)", 
                                     variable=self.unit_var, value="imperial",
                                     bg=self.colors['card'], fg=self.colors['text'],
                                     font=('Segoe UI', 11),
                                     selectcolor=self.colors['card'],
                                     activebackground=self.colors['card'],
                                     cursor='hand2')
        imperial_rb.pack(anchor='w', pady=5)
        
        # Calculation Type Card
        calc_card = self.create_card(self.scrollable_frame, "🧮 Calculation Type")
        
        self.calc_var = tk.StringVar()
        
        diameter_frame = tk.Frame(calc_card, bg=self.colors['card'])
        diameter_frame.pack(fill=tk.X, pady=8)
        
        diameter_rb = tk.Radiobutton(diameter_frame, text="Diameter", 
                                     variable=self.calc_var, value="diameter",
                                     bg=self.colors['card'], fg=self.colors['text'],
                                     font=('Segoe UI', 12),
                                     selectcolor=self.colors['card'],
                                     activebackground=self.colors['card'],
                                     cursor='hand2')
        diameter_rb.pack(side=tk.LEFT)
        
        diameter_formula = tk.Label(diameter_frame, text="2 × radius", 
                                    bg=self.colors['card'], 
                                    fg=self.colors['text_light'],
                                    font=('Segoe UI', 10, 'italic'))
        diameter_formula.pack(side=tk.RIGHT)
        
        circ_frame = tk.Frame(calc_card, bg=self.colors['card'])
        circ_frame.pack(fill=tk.X, pady=8)
        
        circ_rb = tk.Radiobutton(circ_frame, text="Circumference", 
                                 variable=self.calc_var, value="circumference",
                                 bg=self.colors['card'], fg=self.colors['text'],
                                 font=('Segoe UI', 12),
                                 selectcolor=self.colors['card'],
                                 activebackground=self.colors['card'],
                                 cursor='hand2')
        circ_rb.pack(side=tk.LEFT)
        
        circ_formula = tk.Label(circ_frame, text="2πr", 
                                bg=self.colors['card'], 
                                fg=self.colors['text_light'],
                                font=('Segoe UI', 10, 'italic'))
        circ_formula.pack(side=tk.RIGHT)
        
        area_frame = tk.Frame(calc_card, bg=self.colors['card'])
        area_frame.pack(fill=tk.X, pady=8)
        
        area_rb = tk.Radiobutton(area_frame, text="Area", 
                                 variable=self.calc_var, value="area",
                                 bg=self.colors['card'], fg=self.colors['text'],
                                 font=('Segoe UI', 12),
                                 selectcolor=self.colors['card'],
                                 activebackground=self.colors['card'],
                                 cursor='hand2')
        area_rb.pack(side=tk.LEFT)
        
        area_formula = tk.Label(area_frame, text="πr²", 
                                bg=self.colors['card'], 
                                fg=self.colors['text_light'],
                                font=('Segoe UI', 10, 'italic'))
        area_formula.pack(side=tk.RIGHT)
        
        # Action Buttons Card
        action_card = self.create_card(self.scrollable_frame, "⚡ Actions")
        
        button_container = tk.Frame(action_card, bg=self.colors['card'])
        button_container.pack(fill=tk.X, pady=10)
        
        self.calc_btn = tk.Button(button_container, text="Calculate", 
                                  command=self.calculate,
                                  font=('Segoe UI', 11, 'bold'),
                                  bg=self.colors['primary'], 
                                  fg='white',
                                  relief=tk.FLAT, bd=0,
                                  cursor='hand2',
                                  activebackground=self.colors['primary_hover'],
                                  activeforeground='white')
        self.calc_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        
        clear_btn = tk.Button(button_container, text="Clear All", 
                              command=self.clear_all,
                              font=('Segoe UI', 11, 'bold'),
                              bg=self.colors['card'], 
                              fg=self.colors['text'],
                              relief=tk.FLAT, bd=1,
                              cursor='hand2',
                              activebackground=self.colors['border'],
                              activeforeground=self.colors['text'])
        clear_btn.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5, 0))
        
        # Result Card
        result_card = self.create_card(self.scrollable_frame, "✨ Result")
        
        self.result_label = tk.Label(result_card, text="Ready to calculate...",
                                     font=('Segoe UI', 12),
                                     bg=self.colors['card'], fg=self.colors['text_light'],
                                     wraplength=450, justify=tk.CENTER)
        self.result_label.pack(pady=20)
        
        self.error_label = tk.Label(self.scrollable_frame, text="",
                                    font=('Segoe UI', 10),
                                    bg=self.colors['bg'], fg=self.colors['danger'])
        self.error_label.pack(pady=(0, 10))
        
        ref_card = self.create_card(self.scrollable_frame, "📖 Quick Reference")
        
        ref_text = """• Diameter = 2 × radius
• Circumference = 2πr (π ≈ 3.14159)
• Area = πr²

💡 Tip: Press 'Enter' to calculate quickly!"""
        
        ref_label = tk.Label(ref_card, text=ref_text,
                            font=('Segoe UI', 10),
                            bg=self.colors['card'], fg=self.colors['text_light'],
                            justify=tk.LEFT)
        ref_label.pack(pady=10, anchor='w')
        
    def setup_shortcuts(self):
        """Setup keyboard shortcuts"""
        self.app.bind('<Return>', lambda event: self.calculate())
        self.app.bind('<Escape>', lambda event: self.clear_all())
        
    def validate_radius(self, value):
        """Validate radius input"""
        if not value or value.strip() == "":
            return False, "Please enter a radius value", None
        
        try:
            radius = float(value)
        except ValueError:
            return False, "Please enter a valid number (e.g., 5, 2.5, 10.75)", None
        
        if radius < 0:
            return False, "Radius cannot be negative", None
        
        if radius == 0:
            return True, "Radius is zero. The circle would be a point.", 0.0
        
        return True, None, radius
    
    def calculate(self):
        """Perform calculation"""
        self.error_label.config(text="")
        
        radius_text = self.radius_entry.get()
        is_valid, error_msg, radius = self.validate_radius(radius_text)
        
        if not is_valid:
            self.error_label.config(text=error_msg)
            self.result_label.config(text="Invalid input", fg=self.colors['danger'])
            return
        
        if error_msg:
            self.error_label.config(text=error_msg)
        
        calc_type = self.calc_var.get()
        if not calc_type:
            self.error_label.config(text="Please select a calculation type")
            self.result_label.config(text="Selection required", fg=self.colors['text_light'])
            return
        
        if calc_type == "diameter":
            result = 2 * radius
            formula = "Diameter = 2 × radius"
            calc_name = "Diameter"
        elif calc_type == "circumference":
            result = 2 * math.pi * radius
            formula = "Circumference = 2πr"
            calc_name = "Circumference"
        else:
            result = math.pi * (radius ** 2)
            formula = "Area = πr²"
            calc_name = "Area"
        
        if result < 0.01:
            result_str = f"{result:.6f}"
        elif result < 1:
            result_str = f"{result:.4f}"
        elif result < 1000:
            result_str = f"{result:.2f}"
        else:
            result_str = f"{result:.1f}"
        
        unit_system = self.unit_var.get()
        if calc_type == "area":
            unit = "cm²" if unit_system == "metric" else "in²"
        else:
            unit = "cm" if unit_system == "metric" else "in"
        
        result_text = f"""🎉 {calc_name}: {result_str} {unit}

📐 Radius: {radius} {"cm" if unit_system == "metric" else "in"}
📝 Formula: {formula}
✨ π = 3.14159"""
        
        self.result_label.config(text=result_text, fg=self.colors['text'])
        self.error_label.config(text="✅ Calculation complete!", fg=self.colors['secondary'])
        
        self.app.after(2000, lambda: self.clear_success_message())
    
    def clear_success_message(self):
        """Clear success message after delay"""
        if self.error_label.cget("text") == "✅ Calculation complete!":
            self.error_label.config(text="")
    
    def clear_all(self):
        """Clear all inputs"""
        self.radius_entry.delete(0, tk.END)
        self.calc_var.set("")
        self.result_label.config(text="Ready to calculate...", fg=self.colors['text_light'])
        self.error_label.config(text="✨ All cleared! Ready for new calculation")
        self.radius_entry.focus_set()
        
        self.app.after(2000, lambda: self.clear_success_message())
    
    def run(self):
        """Run the application"""
        self.app.update_idletasks()
        x = (self.app.winfo_screenwidth() // 2) - (550 // 2)
        y = (self.app.winfo_screenheight() // 2) - (750 // 2)
        self.app.geometry(f'+{x}+{y}')
        
        self.app.mainloop()


if __name__ == "__main__":
    app = CirclifyApp()
    app.run()
