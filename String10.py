def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    a = x*y
    return f'({x}+{y})*{2}={a}'
print(main(3, 5))