"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""
"""
Sample Test Case:

Input - 10
Output - 23

Input - 1000
Output - 233168
"""

def solution(n):
    # Returns the sum of all the multiples of 3 or 5 below n.

    return sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0])


if __name__ == "__main__":
    print(solution(int(input())))
