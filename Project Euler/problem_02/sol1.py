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
    i = 1
    j = 2
    sum = 0
    while j <= n:
        if j % 2 == 0:
            sum += j
        i, j = j, i + j

    return sum


if __name__ == "__main__":
    print(solution(int(input().strip())))
