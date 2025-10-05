def safe_divide(numerator, denominator):
    """
    Performs a safe division operation between two numbers.
    Handles:
      - Division by zero (ZeroDivisionError)
      - Non-numeric inputs (ValueError)
    Returns:
      - A success message with the result if valid.
      - An error message string if an exception occurs.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Attempt division
        result = num / denom
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
