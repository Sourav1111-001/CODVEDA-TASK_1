import os
try:
    import importlib
    colorama = importlib.import_module("colorama")
    Fore = colorama.Fore
    Style = colorama.Style
    init = colorama.init
    # Initialize Colorama
    init(autoreset=True)
except Exception:
    # colorama not available — provide no-op replacements so the script still runs
    class _NoColor:
        def __getattr__(self, name):
            return ""
    Fore = Style = _NoColor()
    def init(*args, **kwargs):
        return None

# Functions for operations
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def calculator():
    while True:
        clear_screen()
        print(Fore.CYAN + "="*40)
        print(Fore.YELLOW + "        🧮 SIMPLE PYTHON CALCULATOR")
        print(Fore.CYAN + "="*40)
        print(Fore.GREEN + """
        [1] ➕ Addition
        [2] ➖ Subtraction
        [3] ✖ Multiplication
        [4] ➗ Division
        [5] ❌ Exit
        """)
        
        choice = input(Fore.MAGENTA + "👉 Enter choice (1-5): ")

        if choice == '5':
            print(Fore.RED + "Goodbye! 👋")
            break

        try:
            num1 = float(input(Fore.BLUE + "Enter first number: "))
            num2 = float(input(Fore.BLUE + "Enter second number: "))
            
            if choice == '1':
                result = add(num1, num2)
                symbol = "+"
            elif choice == '2':
                result = subtract(num1, num2)
                symbol = "-"
            elif choice == '3':
                result = multiply(num1, num2)
                symbol = "×"
            elif choice == '4':
                result = divide(num1, num2)
                symbol = "÷"
            else:
                print(Fore.RED + "⚠ Invalid choice!")
                input("Press Enter to continue...")
                continue
            
            print(Fore.CYAN + f"\n✨ Result: {num1} {symbol} {num2} = {result}")
        
        except ValueError:
            print(Fore.RED + "⚠ Invalid input! Please enter numbers only.")
        
        input(Fore.YELLOW + "\n🔄 Press Enter to continue...")

# Run the calculator
calculator()
