def calculate(a, b, operation):
    """Calculate using the new argument order: (left operand, right operand, operation)."""
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    elif operation == 'modulo':
        if b == 0:
            return "Error: Cannot calculate modulo by zero"
        return a % b
    else:
        return "Error: Unsupported operation"


# Breaking API change in 2.0.0: operands now come before the operation.
if __name__ == "__main__":
    print(calculate(5, 3, 'add'))        # 8
    print(calculate(5, 3, 'subtract'))   # 2
    print(calculate(5, 3, 'multiply'))   # 15
    print(calculate(5, 3, 'divide'))     # 1.666...
    print(calculate(5, 0, 'divide'))     # Error: Cannot divide by zero
    print(calculate(5, 3, 'modulo'))     # 2
