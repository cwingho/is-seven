def is_seven(number):
    """
    Check if a number equals 7.
    
    Args:
        number: A value to check. Can be:
               - Integer
               - Float 
               - String (will attempt conversion)
               - Complex number (real part only)
        
    Returns:
        bool: True if the number is 7, False otherwise
    """
    # Handle strings
    if isinstance(number, str):
        if number.lower() == "seven":
            return True
        try:
            number = float(number)
        except ValueError:
            return False
            
    # Handle complex numbers
    if isinstance(number, complex):
        number = number.real
        
    # Handle numeric types
    if isinstance(number, (int, float)):
        return abs(number - 7) < 1e-10
        
    return False