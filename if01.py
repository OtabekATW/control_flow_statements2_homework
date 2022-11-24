def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    r = 0
    if a > b:
        if a > c:
            r = a
    else :
        if b > c:
            r = b
        r = c            

    return r