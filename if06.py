def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """

    x1 = n % 10
    n = n // 10
    
    x2 = n % 10
    n = n // 10

    x3 = n % 10
    n = n // 10

    x4 = n % 10
    n = n // 10

    x5 = n % 10

    idx = 0
    mx = x5
    if mx < x4:
        mx = x4
        idx = 1
    if mx < x3:
        mx = x3
        idx = 2
    if mx < x2:
        mx = x2
        idx = 3
    if mx < x1:
        mx = x1
        idx = 4
    return idx