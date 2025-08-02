"""" 
Python module for handling basic calculation operations 
"""

# Function to perform addition
def add(num1, num2):
    """Handles addition"""
    return float(num1 + num2)

# Function to perform subtraction
def subtract(num1, num2):
    """Handles subtraction"""
    return float(num1 - num2)

# Function to perform multiplication
def multiply(num1, num2):
    """Handles multiplication"""
    return float(num1 * num2)

# Function to perform division with built-in error handling in main
def divide(num1, num2):
    """Handles division; raises error if dividing by zero"""
    return float(num1 / num2)

def main():
    # Prompt user for two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Prompt user for an arithmetic operator
    operator = input("Enter the operator you want to calculate with (*, +, -, /): ")
    
    # Pre-compute operations except division (which might raise error)
    operations = {
        "*": multiply(num1, num2),
        "+": add(num1, num2),
        "-": subtract(num1, num2)
    }

    # Format string representation of the operation
    string_rep = f"{num1} {operator} {num2} ="
    
    # Use match-case to select and execute the operation
    match operator:
        case "*":
            print(string_rep, operations["*"])
        case "+":
            print(string_rep, operations["+"])
        case "-":
            print(string_rep, operations["-"])
        case "/":
            if num2 == 0:
                raise ValueError("Can't divide by zero")
            print(string_rep, divide(num1, num2))
        case _:
            print("Unsupported operator. Please use +, -, *, or /.")

# Run the main function if the file is executed directly
if __name__ == "__main__":
    main()

