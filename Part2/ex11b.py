# Create a function called calculate that takes three arguments:
# - number1, operator, number2
# It should return the result of the calculation

def calculate(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Test the function with different operations
print(calculate(10, "+", 10))  # Output: 20
print(calculate(10, "-", 10))  # Output: 0
print(calculate(10, "*", 10))  # Output: 100
print(calculate(10, "/", 10))  # Output: 1.0
