import art

# ------------------ Functions for Operations ------------------

def addition(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."  # Prevents crashing
    return n1 / n2

# Dictionary to map operation symbols to corresponding functions
operations = {
    "+" : addition,
    "-" : subtract,
    "*" : multiply,
    "/" : division
}

# ------------------ Calculator Logic ------------------
def calculator():
    # Print the logo from art.py
    print(art.logo)

    # Take first number input from user
    num1 = float(input("Enter the First Number: "))
    should_accumulate = True  # Flag to continue or reset calculation
    
    while should_accumulate:
        # Show available operations
        for symbol in operations:
            print(symbol)
        
        # Ask user which operation to perform
        operation_symbol = input("Pick an Operation: ")
        num2 = float(input("Enter the Next Number: "))  # Get second number
        
        # Select the function from the dictionary
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)  # Perform calculation

        # Display result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask if the user wants to continue with the current result
        choice = input(
            f"Type 'yes' to continue calculating with {answer}, "
            "or 'no' to start a new calculation: ").lower()

        if choice == "yes":
            # Continue using current answer as the first number
            num1 = answer
            
        else:
            # Stop current calculation loop and restart calculator fresh
            should_accumulate = False
            calculator()

# ------------------ Run the Calculator ------------------
calculator()
