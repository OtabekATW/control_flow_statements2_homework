def main(n):
    """
    Find the largest digit of the five-digit number.
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

    r = 0

    if x1 > x2:
        if x1 > x3:
            if x1 > x4:
                if x1 > x5:
                    r = x1
                else:
                    r = x5
            else:
                if x4 > x5:
                    r = x4
                else:
                    r = x5         
        else:
            if x3 > x4:
                if x3 > x5:
                    r = x3
                else:
                    r = x5
            else:
                if x4 > x5:
                    r = x4
                else:
                    r = x5
    else:
        if x2 > x3:
            if x2 > x4:
                if x2 > x5:
                    r = x2
                else:
                    r = x5
            else:
                if x4 > x5:
                    r = x4
                else:
                    r = x5
        else:
            if x3 > x4:
                if x3 > x5:
                    r = x3
                else:
                    r = x5
            else:
                if x4 > x5:
                    r = x4
                else:
                    r = x5                                      

    return r