def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    min = 0
    if a < b:
        if a < c:
            min = a
        else:
            min = c
    else:
        if b < c:
            min = b
        else:
            min = c            

    return min 