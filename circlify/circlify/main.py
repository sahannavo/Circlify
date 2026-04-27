"""Main entry point for Circlify"""

from .app import CirclifyApp

def main():
    """Start the Circlify application"""
    app = CirclifyApp()
    app.run()

if __name__ == "__main__":
    main()