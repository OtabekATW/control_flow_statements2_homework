def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a == b:
        r = 0
    else:
        if a > b:
            r = a
        else:
            r = b    
    return r