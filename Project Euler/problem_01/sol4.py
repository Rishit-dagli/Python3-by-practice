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

    xmulti = []
    zmulti = []
    z = 3
    x = 5
    temp = 1
    while True:
        result = z * temp
        if result < n:
            zmulti.append(result)
            temp += 1
        else:
            temp = 1
            break
    while True:
        result = x * temp
        if result < n:
            xmulti.append(result)
            temp += 1
        else:
            break
    collection = list(set(xmulti + zmulti))
    return sum(collection)


if __name__ == "__main__":
    print(solution(int(input())))