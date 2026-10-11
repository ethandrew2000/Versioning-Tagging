def calculate(a, b, operation):
    """Return a result object; the 3.0 API no longer returns bare values or error strings."""
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
    else:
        return {"success": False, "error": "Unsupported operation"}

    return {"success": True, "result": result}


# Breaking API change in 3.0.0: results now use a dictionary response.
if __name__ == "__main__":
    print(calculate(5, 3, 'add'))       # {'success': True, 'result': 8}
    print(calculate(5, 0, 'divide'))    # {'success': False, 'error': 'Cannot divide by zero'}
    print(calculate(5, 3, 'modulo'))    # {'success': True, 'result': 2}
