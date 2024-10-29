def is_seven(number):
    """
    Check if a number is seven.
    
    Args:
        number: The value to test. Can be an integer, float, string.
        
    Returns:
        bool: True if the input is seven, False otherwise.
    """
    if isinstance(number, (int, float)):
        return number == 7
    elif isinstance(number, str):
        try:
            return float(number) == 7
        except ValueError:
            return False
    return False