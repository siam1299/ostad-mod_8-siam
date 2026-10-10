def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def safe_calculate(operation, a, b):
    try:
        if operation == "add":
            return add(a, b)
        elif operation == "subtract":
            return subtract(a, b)
        elif operation == "multiply":
            return multiply(a, b)
        else:
            raise ValueError("Unsupported operation")
    except TypeError:
        return "Error: Please provide valid numbers"
    except ValueError as error:
        return f"Error: {error}"