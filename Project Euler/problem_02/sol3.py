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
    """
    if n <= 1:
        return 0
    a = 0
    b = 2
    count = 0
    while 4 * b + a <= n:
        a, b = b, 4 * b + a
        count += a
    return count + b


if __name__ == "__main__":
    print(solution(int(input().strip())))
