"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3,5,6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""

"""
Sample Test Cases:

Input - 1000
Output - 233168

Input - 19564
Output - 89301183
"""

def solution(n):
    # Returns the sum of all the multiples of 3 or 5 below n.

    return sum([i for i in range(3, n) if i % 3 == 0 or i % 5 == 0])


if __name__ == "__main__":
    print(solution(int(input())))