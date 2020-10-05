def solution(n):
    """Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """

    sum = 0
    terms = (n - 1) // 3
    sum += ((terms) * (6 + (terms - 1) * 3)) // 2  # sum of an A.P.
    terms = (n - 1) // 5
    sum += ((terms) * (10 + (terms - 1) * 5)) // 2
    terms = (n - 1) // 15
    sum -= ((terms) * (30 + (terms - 1) * 15)) // 2
    return sum


if __name__ == "__main__":
    print(solution(int(input().strip())))
