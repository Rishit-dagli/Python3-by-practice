import math
from decimal import Decimal, getcontext


def solution(n):
    """Returns the sum of all fibonacci sequence even elements that are lower
    or equals to n.

    >>> solution(10)
    10
    >>> solution(15)
    10
    >>> solution(2)
    2
    >>> solution(1)
    0
    >>> solution(34)
    44
    >>> solution(3.4)
    2
    >>> solution(0)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater or equal to one.
    >>> solution(-17)
    Traceback (most recent call last):
        ...
    ValueError: Parameter n must be greater or equal to one.
    >>> solution([])
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or passive of cast to int.
    >>> solution("asd")
    Traceback (most recent call last):
        ...
    TypeError: Parameter n must be int or passive of cast to int.
    """
    try:
        n = int(n)
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or passive of cast to int.")
    if n <= 0:
        raise ValueError("Parameter n must be greater or equal to one.")
    getcontext().prec = 100
    phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2)

    index = (math.floor(math.log(n * (phi + 2), phi) - 1) // 3) * 3 + 2
    num = Decimal(round(phi ** Decimal(index + 1))) / (phi + 2)
    sum = num // 2
    return int(sum)


if __name__ == "__main__":
    print(solution(int(input().strip())))
