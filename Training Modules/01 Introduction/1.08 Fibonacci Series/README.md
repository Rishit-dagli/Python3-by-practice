# Fibonacci Sequence
Original problem link: https://www.faceprep.in/python/fibonacci-series-in-python/
 
Fibonacci series is a series in which each number is the sum of the preceding two numbers. By default, the first two numbers of a Fibonacci series are 0 and 1

## Input Format:

Input consists of an integer

# Output Format:

A single line of output containing the Fibonacci series until 7 values.

SAMPLE INPUT:

```
7
```

SAMPLE OUTPUT:

```
0 1 1 2 3 5 8
```

## Pseudo code

Step 1:Input the 'n' value until which the Fibonacci series has to be generated

Step 2:Initialize sum = 0, a = 0, b = 1 and count = 1

Step 3:while (count <= n)

Step 4:print sum

Step 5:Increment the count variable

Step 6:swap a and b

Step 7:sum = a + b

Step 8:while (count > n)

Step 9:End the algorithm

Step 10:Else

Step 11:Repeat from steps 4 to 7
