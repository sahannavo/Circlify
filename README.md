# Circlify

A modern, human-centered circle calculator with an intuitive graphical interface built with Python and Tkinter.

## Features

- **Circle Calculations**: Compute diameter, circumference, and area from radius
- **Unit Systems**: Support for metric (cm/m) and imperial (in/ft) units
- **Modern UI**: Clean, responsive interface with scrollable content
- **Input Validation**: Friendly error messages and real-time feedback
- **Keyboard Shortcuts**: Press `Enter` to calculate, `Escape` to clear
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Screenshots

![Circlify Screenshot 01](https://github.com/sahannavo/Circlify/blob/main/screenshots/img%2001.png?raw=true)
![Circlify Screenshot 02](https://github.com/sahannavo/Circlify/blob/main/screenshots/img%2002.png?raw=true)

## Installation

### Prerequisites

- Python 3.7 or higher
- Tkinter (usually included with Python)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sahannavo/Circlify.git
cd Circlify
```

2. Install dependencies (optional, Tkinter is usually pre-installed):
```bash
pip install -r requirements.txt
```

## Usage

### Run the Application

**Option 1: Direct execution (recommended)**
```bash
python circlify/app.py
```

**Option 2: Using run.py**
```bash
python run.py
```

**Option 3: As a module**
```bash
python -m circlify.main
```

### How to Use

1. Enter the radius value in the input field
2. Select your unit system (Metric or Imperial)
3. Choose calculation type: Diameter, Circumference, or Area
4. Click "Calculate" or press `Enter`
5. View results in the Result card

## Project Structure

```
circlify/
├── circlify/
│   ├── __init__.py          # Package initialization
│   ├── app.py               # Main GUI application (standalone)
│   ├── main.py              # Module entry point
│   ├── core/                # Core business logic
│   │   ├── calculator.py    # Circle calculation algorithms
│   │   ├── validator.py     # Input validation
│   │   └── units.py         # Unit conversion handling
│   ├── ui/                  # UI components
│   │   ├── components.py    # Reusable UI widgets
│   │   └── styles.py        # Styling and theming
│   └── utils/               # Utilities
│       └── constants.py     # App constants and config
├── tests/
│   └── test_calculator.py   # Unit tests
├── docs/                    # Documentation
├── screenshots/             # App screenshots
├── modern_calculator.py     # Alternative standalone version
├── run.py                   # Simple runner script
└── setup.py                 # Package setup
```

## Development

### Running Tests

```bash
python -m unittest tests.test_calculator -v
```

### Code Organization

- **Core Logic**: Located in `circlify/core/` - handles calculations, validation, and units
- **UI Layer**: Located in `circlify/ui/` - manages components and styling
- **Entry Points**: `app.py` (standalone), `main.py` (module), `run.py` (simple runner)

## API Reference

### CircleCalculator

```python
from circlify.core.calculator import CircleCalculator

calculator = CircleCalculator()

# Calculate diameter
diameter = calculator.calculate_diameter(5)  # Returns: 10

# Calculate circumference
circumference = calculator.calculate_circumference(5)  # Returns: 31.4159...

# Calculate area
area = calculator.calculate_area(5)  # Returns: 78.5398...
```

### Validator

```python
from circlify.core.validator import Validator

validator = Validator()

# Validate radius
is_valid, error_msg, radius = validator.validate_radius("5.5")
# Returns: (True, None, 5.5)
```

## Formulas

- **Diameter**: `D = 2 × r`
- **Circumference**: `C = 2πr` (π ≈ 3.14159)
- **Area**: `A = πr²`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- **Your Name** - [GitHub](https://github.com/sahannavo)

## Acknowledgments

- Built with Python and Tkinter
- Modern UI design inspired by contemporary calculator apps
