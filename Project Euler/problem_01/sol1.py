def solution(n):
   """ Returns the sum of all the multiples of 3 or 5 below n.

    >>> solution(3)
    0
    >>> solution(4)
    3
    >>> solution(10)
    23
    >>> solution(600)
    83700
    """
   return sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0])


if __name__ == "__main__":
   print(solution(int(input())))
