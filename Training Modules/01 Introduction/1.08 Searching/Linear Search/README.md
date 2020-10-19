***LINEAR SEARCH-***

A linear search, also known as a sequential search, is a method of finding an element within a list.

It checks each element of the list sequentially until a match is found or the whole list has been searched.

***TASK-***
To search an element using linear search.

1. Create a function searching that takes a list, size and key as arguemnts.

2. A loop iterates through the list and when an item matching the key is found, the corresponding index is returned.

3. If no such item is found, -1 is returned.


***SAMPLE INPUT-***

Enter no. of elements=5

enter element=22

enter element=54

enter element=68

enter element=79

enter element=81

element to be searched=79


***SAMPLE OUTPUT-***

element present at 4


***TO REMEMBER-***

Best case = search value present at the first   position = O(1)

Worst case = search value not present  = O(n)

Average case = search value present at the ith position = O(n)

Works on any random list
