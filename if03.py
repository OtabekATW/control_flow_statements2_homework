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
    mx =  a
    if mx > b:
        mx = b
    if mx > c:
        mx = c

    mn = a
    if mn < b:
        mn = b
    if mn < c:
        mn = c
    
    return a + b + c - mx - mn