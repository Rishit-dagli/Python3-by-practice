def solution(n):
    '''
    This function returns the difference between the sum of the squares of the first n (given by user) natural numbers and the square of their sum
    for example :
    >>> solution(10)
    2640
    >>> solution(50)
    1582700
    >>> solution(100)
    25164150
    '''
    sumBeforeSqure = (((n+1)*n)/2)**2
    sumAfterSqure = (n*(n+1)*(2*n + 1))/6
    result = int(sumBeforeSqure-sumAfterSqure)
    return result


if __name__ == "__main__":
    print(solution(int(input())))
    
    
