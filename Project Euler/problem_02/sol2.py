def solution(n):
    """Returns the sum of all fibonacci sequence even elements that are lower
    or equals to n.

    >>> solution(10)
    [2, 8]
    >>> solution(15)
    [2, 8]
    >>> solution(2)
    [2]
    >>> solution(1)
    []
    >>> solution(34)
    [2, 8, 34]
    """
    ls = []
    a, b = 0, 1
    while b <= n:
        if b % 2 == 0:
            ls.append(b)
        a, b = b, a + b
    return ls


if __name__ == "__main__":
    print(solution(int(input().strip())))
