"""" Python module for handling  basic calculations operations """

num1 = int(input("Enter the first number: "))  # prompt user for the fisrt number
num2 = int(input("Enter the second number: ")) # Prompt for the second number

operator = input("Enter the operator you want your number to be calculated with (*, +, -, / ): ") # Prompt user for operators
string_rep = f"{num1} {operator} {num2} ="
match operator:

    case "*": # handles multiplication
        print(string_rep, num1 * num2) 

    case "+":# handles addition
        print(string_rep, num1 + num2)

    case "-": # handles subtraction
        print(string_rep, num1 - num2)

    case "/": # handle for division and raises an error if user tries dividing by zero
        if num2 == 0:
            raise ValueError("Can't divide by zero")
        print(string_rep, num1 / num2)
