def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    r = 0
    if a > b:
        if a < c:
            r = a
        else:
            if b > c:
                r = b
    else:
        if a > c:
            r = a
        else:
            r = c                

    return r