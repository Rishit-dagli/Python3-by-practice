***BINARY SEARCH-***

In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted by ignoring half of the elements after just one comparison.

-Compare x with the middle element.

-If x matches with the middle element, we return the mid index.

-Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray after the mid element. Then we apply the algorithm again for the right half.

-Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.

***TASK-***
To search an element using recursive binary search.

***SAMPLE INPUT-***

Enter no. of elements=5

enter element=12

enter element=32

enter element=46

enter element=75

enter element=89

element to be searched=75


***SAMPLE OUTPUT-***

element present at 4


***TO REMEMBER-***
best case= search value present at the middle= O(1)

Worse case = search value not present = O(log n)

Works only on ascending order list
