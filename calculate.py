def calculate(a, b, operation):
    """Return a structured result for a supported arithmetic operation."""
    if operation == 'add':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            return {"success": False, "error": "Cannot divide by zero"}
        result = a / b
    elif operation == 'modulo':
        if b == 0:
            return {"success": False, "error": "Cannot calculate modulo by zero"}
        result = a % b
    elif operation == 'power':
        result = a ** b
    else:
        return {"success": False, "error": "Unsupported operation"}

    return {"success": True, "result": result}


# Example usage
if __name__ == "__main__":
    print(calculate(2, 3, 'power'))     # {'success': True, 'result': 8}
    print(calculate(5, 3, 'add'))       # {'success': True, 'result': 8}
    print(calculate(5, 0, 'divide'))    # {'success': False, 'error': 'Cannot divide by zero'}
