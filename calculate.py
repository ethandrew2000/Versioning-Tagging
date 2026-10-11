import math


def _is_valid_number(value):
    """Accept finite integers and floats, but reject booleans and non-numeric values."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return False
    return not isinstance(value, float) or math.isfinite(value)


def calculate(a, b, operation):
    """Return a structured result after validating inputs and the calculated value."""
    if not _is_valid_number(a) or not _is_valid_number(b):
        return {"success": False, "error": "Operands must be finite integers or floats"}
    if not isinstance(operation, str):
        return {"success": False, "error": "Operation must be a string"}

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
        try:
            result = a ** b
        except (ArithmeticError, ValueError):
            return {"success": False, "error": "Operation is outside the supported numeric range"}
    else:
        return {"success": False, "error": "Unsupported operation"}

    if isinstance(result, complex):
        return {"success": False, "error": "Operation must produce a real number"}
    if isinstance(result, float) and not math.isfinite(result):
        return {"success": False, "error": "Result must be finite"}

    return {"success": True, "result": result}


# Example usage
if __name__ == "__main__":
    print(calculate(2, 3, 'power'))       # {'success': True, 'result': 8}
    print(calculate("2", 3, 'add'))       # Validation error
    print(calculate(5, 0, 'divide'))      # Division-by-zero error
