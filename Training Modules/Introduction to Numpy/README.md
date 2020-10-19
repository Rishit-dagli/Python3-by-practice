![Numpy](https://miro.medium.com/max/765/1*cyXCE-JcBelTyrK-58w6_Q.png)
# NumPy
NumPy **(Numerical Python)** is an open source Python library that’s used  for working with numerical data in Python.
It is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python.

Numpy can also be used as an efficient multi-dimensional container of generic data.

## Pre-Requisites
* Basic working knowledge of Python.

## Basic things to know before we start with the topic:
In the Numpy definition, you read that they basically work with **Arrays** so what are **Arrays**???
### Arrays
* An array is a collection of items stored at continuous memory locations.
* All the stored items should be of same type.

![Array](https://media.geeksforgeeks.org/wp-content/uploads/array-2.png)
Source: GeeksforGeeks

Arrays are of two types:
* One-Dimensional Array
* Multi-Dimensional Array
#### One-Dimensional Array
A one-dimensional array (or single dimension array) is a type of linear array.Accessing its elements involves a single subscript which can either represent a row or column index.
Example:
```
   # A character array in C/C++/Java
   char arr1[] = {'D','e','v','I','n','c','e','p','t'};
   
   # An Integer array in C/C++/Java
   int arr2[] = {10, 20, 30, 40, 50};
  ``` 
  > To access the elements of a **single-dimensional** Array you can use the **indexes** and most of the Arrays are  **zero-indexed.**
 ```
  arr1[0]; # gives us D
  arr1[2]; # gives us v
  arr2[1]; # gives us 20
  arr2[4]; # gives us 50
 ```
 > **Note:** Array of characters is called a string.
 > Yes!! These are the same strings which we use in Pyhton they are also Arrayss hidden in plain sight.
 
#### Multi-Dimensional Arrays
A multi-dimensional array is an array with more than one level or dimension. For example, a 2D array, or two-dimensional array.
**Meaning it is a matrix of rows and columns (think of a table).**

![2-D Array](https://cdn.programiz.com/sites/tutorial2program/files/2d-array-variable-length.jpg)

Example:
```
  int two_d[10][20];
  int x[3][4] = {{0,1,2,3}, {4,5,6,7}, {8,9,10,11}};
  char y[3][4] = {{'a','b','c','d'}, {'D','e','V','I'}, {'n','c','e','p'}};
```  
> To access the elements of a **multi-dimensional** Array you can use the **indexes** and most of the Arrays are  **zero-indexed.**

```
  x[0][1]; # gives us 1
  y[1][2]; # gives us V
```
> You can access elements in a multi-dimensional like in the example showed above..

# Attention!! Python Lists are also kind of Arrays but more easy....
## As *Python* makes everything easy.. :smirk::smirk:
Few simple Examples:
```python
  list=['DevIncept',10,'Sam',100,20]
  print(list[0])
  print(list[2])
  print(list[3])
 ```
 A Python list may contain different types! Indeed, you can store a number, a string, and even another list within a single list.
Result:
```python
   DevIncept
   Sam
   100
 ```
You can tinker with the above example in the provided Jupyter Notebook..

## Why use NumPy over Pyhton Lists???
* ### In Python we have lists that serve the purpose of arrays, but they are slow to process.
* ### NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.
* ### Arrays are very frequently used in data science, where speed and resources are very important.

**Note:**
>  All of the elements in a NumPy array should be homogeneous.


## Installing NumPy
### Attention!!! You must already have Python:snake: installed in order to install Numpy.
If you already have Python, you can install NumPy with:
```python
   pip install numpy
```
**Or**
```python
   conda install numpy
  ```
 If you don’t have Python yet, you might want to consider using [Anaconda](https://www.anaconda.com/). It’s the easiest way to get started.


## How to Import Numpy
Any time you want to use a package or library in your code, you first need to make it accessible.
In order to start using NumPy and all of the functions available in NumPy, you’ll need to import it. This can be easily done with this import statement:
```python
   import numpy as np
 ```
> (You can use any variable instead of **np**) 

# Attention!!!  Attention!!! Attention!!
## Those who have problems installing Pyhton on PCs or have problem Installing Jupyter Notebooks and using them.Instead of that you can use [Google Colab](https://colab.research.google.com/) its a jupyter notebook on cloud which anyone can use and its free.Its fast and you can do all the coding you want in there.:smile::smiley: 

*******
*******
# NumPy Basics:
## Creating a basic Array
To create a basic NumPy Array you can use the function ***np.array()***
The array object in NumPy is called **ndarray**
```python
   import numpy as np
   arr1=np.array([1,2,3])
   arr2=np.array(['a','b','c','d','e'])
   arr3= np.array((1, 2, 3, 4, 5)) # You can also pass a tuple to creat an Array
   print(arr1)
   print(arr2)
   print(arr3)
   print(type(arr1))
 ```
**Result:**
```python
   [1 2 3]
   ['a' 'b' 'c' 'd' 'e']
   [1 2 3 4 5]
   <class 'numpy.ndarray'>
  ```
  
  ![arr1](https://numpy.org/devdocs/_images/np_array.png)
  
  
  **Besides the above examples you can create Arrays using builtin function**
  * To create an Array of Zeroes use ***np.zeros()***
  * To create an Array of Ones use ***np.ones()***
  * To create an Array with a range of elements use ***np.arange()***
  ```python
     import numpy as np
     a=np.zeros(3)
     b=np.ones(5)
     c=np.arange(10)
     d=np.arange(2,9)   # To specify start and stop
     e=np.arange(1,10,2) # To specify start and stop with step size
     print(a)
     print(b)
     print(c)
     print(d)
     print(e)
  ``` 
  **Result:**
  ```python
     [ 0.  0.  0.]
     [ 1.  1.  1.  1.  1.]
     [0 1 2 3 4 5 6 7 8 9]
     [2 3 4 5 6 7 8]
     [1 3 5 7 9]
  ```  
  > **You can try the code yourself in the provided Jupyter Notebook**


## NdArray(N-Dimensional Array)
1. An array class in Numpy is called as **ndarray**.
2. Number of dimensions of the array is called rank of the array.

**Lets Create a 2-D(Dimensional) Array**
* They are like a matrix or you can say a table
```python
   import numpy as np
   arr1=np.array([[1,2,3],[4,5,6]])
   arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
   arr3=np.array([['a','b','c'],['d','e','f']])
   
   #creates a 3X3 array with all zeros
   zeros=np.zeros((3,3))
   
   #creates a 2X2 array with all ones
   ones=np.ones((2,2),dtype='int64')  #specify the type with (dtype) parameter 
   
   print(arr1)
   print(arr2)
   print(arr3)
   print(zeros)
   print(ones)
```
**Result:**
```python
   [[1 2 3]
    [4 5 6]]
    
   [[1 2 3]
    [4 5 6]
    [7 8 9]] 
    
   [['a' 'b' 'c']
    ['d' 'e' 'f']]
    
   # 3X3 Matrix
   [[ 0.  0.  0.]
    [ 0.  0.  0.]
    [ 0.  0.  0.]]
    
   # 2X2 Matrix
   [[1 1]
    [1 1]]
```    
> NumPy provides some cool methods you can check the number of dimensions using ***ndim***  
```python
   import numpy as np

   a = np.array(42)
   b = np.array([1, 2, 3, 4, 5])
   c = np.array([[1, 2, 3], [4, 5, 6]])
   d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

   print(a.ndim)
   print(b.ndim)
   print(c.ndim)
   print(d.ndim)
``` 
**Result:**
```python
   0
   1
   2
   3
```
## Basic Operations with Arrays
You can also do basic arthemetic operations with arrays.
```python
   import numpy as np
   arr1=np.array([5,5,5,5])
   arr2=np.array([3,3,3,3])
   c=arr1+arr2
   d=arr1-arr2
   e=arr1/arr2
   print(arr1)
   print(arr2)
   print(c) # addition
   print(d) # subtraction
   print(e) # division
   print("Adding one to all elements:",c+1)
   print("Subtracting one from all elements:",d-1)
```
**Result:**
```python
   [5 5 5 5]
   [3 3 3 3]
   [8 8 8 8]
   [2 2 2 2]
   [1.66666667  1.66666667  1.66666667  1.66666667]
   Adding one to all elements: [9 9 9 9]
   Subtracting one from all elements: [1 1 1 1]
```
> You can also do other basic operations. Try them yourself in the Jupyter Notebook provided.

## I know just for basics also this is too much.If you have reached till this point and still not sure, DONT WORRY!!!!
## You can practice all the examples in the Jupyter Notebook provided, Don't just see them, change them put new values and see what happens..
## Try new things and slowly but steadily you will definetly get a good grasp on them..:smile::smile:

****************
****************
# Array Indexing and Slicing
## Array Indexing:
* **Array indexing is the same as accessing an array element.**
* **You can access an array element by referring to its index number.**
```python
   import numpy as np
   arr1= np.array([3,2,3,4])
   arr2= np.array([2,1,1,3])
   arr3= np.array(['D','e','V','I','n','c','e','p','t'])
   arr4= np.array([[1,2,3,4,5], [6,7,8,9,10]])
   print(arr1[0]) # prints first element
   print(arr1[-1]) # prints last element
   print(arr2[2]) # prints third element
   print(arr3[0]) # prints first element
   print(arr4[1][3]) #prints 9
   print(arr4[1,3]) # Or you can use this type 
```
**Result:**
```python
   3
   4
   1
   D
   9
   9
```
## Array Slicing:
![Slicing](https://wtmatter.com/wp-content/uploads/2020/07/NumPy-Array-Slicing-Python-Tutorial.png)
> Array slicing is same as String Slicing so don't worry...

* Slicing in python means taking elements from one given index to another given index.
* We pass slice instead of index like this: `[start:end]`.
* You can also provide Step size as: `[start:end:step]`.

```python
   import numpy as np
   arr1=np.array(['D','e','V','I','n','c','e','p','t'])
   arr2=np.array([1,2,3,4,5,6,7,8,9])
   
   #2-D Slicing
   arr3=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
   
   print(arr1[:3]) # default is taken as 0
   print(arr1[0:3])
   print(arr1[3:]) # taken till the end
   print(arr1[::2])
   
   print(arr2[-4:-1])
   print(arr2[::2]) # step size as 2
   
   # 2-D Slicing
   print(arr3[1,1:4])
   print(arr3[0:2, 2])
   print(arr3[0:2, 1:4])
```
Result:
```python
   ['D' 'e' 'V']
   ['D' 'e' 'V']
   ['I' 'n' 'c' 'e' 'p' 't']
   ['D' 'V' 'n' 'e' 't']
   
   [6 7 8]
   [1 3 5 7 9]
   
   # Go over these results carefully they are bit tricky..
   [7 8 9]
   [3 8]
   [[2 3 4]
    [7 8 9]]
```
### All in one example
```python
   import numpy as np
   data = np.array([1, 2, 3])
   print(data[1])
   print(data[0:2])
   print(data[1:])
   print(data[-2:])
```
**Result:**
```python
   2
   [1 2]
   [2 3]
   [2 3]
```
![visualization](https://numpy.org/devdocs/_images/np_indexing.png)


****************
******************

# Now to the coolest Part of NumPy. :smile::smile:
# NumPy Functions
## Numpy Array Shape:
`ndarray.shape` will display a tuple of integers that indicate the number of elements stored along each dimension of the array. If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).
```python
   import numpy as np
   arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
   arr1= np.array([1,2,3,4])

   print(arr.shape)
   print(arr1.shape)
 ```
**Result:**
```python
   (2, 4)
   (4,)
 ```
 **All In One Example**
```python
   array_example = np.array([[[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0, 1, 2, 3],
                            [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3],
                            [4, 5, 6, 7]]])
 
   print('No of dimensions of the array:',array_example.ndim)     # .ndim for dimensions
   print('Total no of elements of the array:',array_example.size) # .size for size
   print('Shape of the array:',array_example.shape)                # .shape for shape
 ```
 **Result:**
 ```python
    No of dimensions of the array: 3
    Total no of elements of the array: 24
    Shape of the array: (3, 2, 4)
 ```
 ## After knowing the shape of an Array you would be feeling like to reshape it... But can you??:smirk:
 # Yes You can Absolutely...
 ## NumPy Array Reshaping
 Using `arr.reshape()` will give a new shape to an array without changing the data.
 
 Just remember that when you use the reshape method, the array you want to produce needs to have the same number of elements as the original array.
 **Reshape from 1-D to 2-D**
```python
   import numpy as np
   arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
   newarr1 = arr1.reshape(4, 3)
   arr2 = np.array(['D','e','V','I','n','c','e','p','t'])
   newarr2 = arr2.reshape(3,3)
   print(newarr1)
   print(newarr2)
 ```
 **Result:**
 ```python
    [[ 1  2  3]
     [ 4  5  6]
     [ 7  8  9]
     [10 11 12]]
    
    [['D' 'e' 'V']
     ['I' 'n' 'c']
     ['e' 'p' 't']]
 ```
 **Reshape from 1-D to 3-D**
 ```python
    import numpy as np
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    newarr = arr.reshape(2, 3, 2)
    print(newarr)
  ```
 **Result:**
 ```python
    [[[ 1  2]
      [ 3  4]
      [ 5  6]]

     [[ 7  8]
      [ 9 10]
      [11 12]]]
 ```
 ### Can we Reshape into any Shape??
 Yes, as long as the elements required for reshaping are equal in both shapes.
 
 **We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements.**
 
 * We can use `reshape(-1)` to convert mult-dimensional array into 1-D array.  
```python
   import numpy as np
   arr = np.array([[1, 2, 3], [4, 5, 6]])
   newarr = arr.reshape(-1)
   print(newarr)
```
**Result:**
```python
   [1 2 3 4 5 6]
 ```
 
# NumPy Sorting and Searching
## NumPy Sorting
* Sorting means putting elements in an ***ordered sequence.***
* The NumPy ndarray object has a function called `sort()`, that will sort a specified array.
```python
   import numpy as np
   arr1 = np.array([3, 2, 0, 1])
   arr2 = np.array(['red','blue','green'])
   
   # 2-D array
   arr3 = np.array([[3, 2, 4], [5, 0, 1]])
   
   print(np.sort(arr1))
   print(np.sort(arr2))
   print(np.sort(arr3))
```
**Result:**
```python
   [0 1 2 3]
   ['blue' 'green' 'red']
   [[2 3 4]
    [0 1 5]]
```
## NumPy Searching
Searching is an operation or a technique that helps finds the place of a given element or value in the list. Any search is said to be successful or unsuccessful depending upon whether the element that is being searched is found or not.

### 1. where() : 
Returns the indices of the searched value.
```python
   import numpy as np
   arr1 = np.array([1, 2, 3, 4, 5, 4, 4])
   x = np.where(arr1 == 4)
   y = np.where(arr1%2 == 0)
   z = np.where(arr1%2 == 1)
   print(x)
   print(y)
   print(z)
```
**Result:**
```python
   (array([3, 5, 6]),) # Which means that the value 4 is present at index 3, 5, and 6.
   (array([1, 3, 5, 6]),)
   (array([0, 2, 4]),)
 ```
### 2. searchsorted() :
Performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
> The **searchsorted()** method is assumed to be used on sorted arrays.
```python
   import numpy as np
   arr1 = np.array([6, 7, 8, 9])
   x = np.searchsorted(arr1, 7)
   print(x)
   
   # Multiple values
   arr2 = np.array([1, 3, 5, 7])
   y = np.searchsorted(arr2, [2, 4, 6])
   print(y)
```
**Result:**
```python
   1
   
   [1 2 3]
```
**For more advanced sorting and searching example you can follow the link here ---->>** [Advanced Sorting And Searching](https://www.geeksforgeeks.org/numpy-sorting-searching-and-counting/)    
   
   
# Hooray!!! If you are reading this message you have covered a lot of ground and you are not a Novice anymore.. :smile:
# A few more topics to go.
# Keep Going....!!!!


## Mean, Median, Mode
Yes these are the topics you must have studied in High school...You must be wondering what their use.??

To say they are very important and **NumPy** also have functions for them. You can use these function on large data sets and find the answers in just seconds..:smile:

### Mean
* **Mean** - The average value
* To calculate the mean, find the sum of all values, and divide the sum by the number of values.


**As you all know Python makes everything easy see it yourself.**
```python
   import numpy as np
   arr=np.array([19,13,18,21,44,17,12,31,37,8,12,27])
   x=np.mean(arr)
   print(x)
 ```
 **Result:**
 ```python
    21.5833333333
 ```
### Median
* **Median** - The mid point value
* The median value is the value in the middle, after you have sorted all the values.
```python
   import numpy
   # For one value in the middle
   speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
   x = numpy.median(speed)
   print(x)
   
   # For two values in the middle
   speed1 = [99,86,87,88,86,103,87,94,78,77,85,86]
   y = numpy.median(speed1)
   print(y)
```
**Result:**
```python
   87.0
   
   86.5
```

### Mode
* **Mode** - The most common value
* The Mode value is the value that appears the most number of times.

> This function comes under **SciPy**
```python
   from scipy import stats
   speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
   x = stats.mode(speed)
   print(x)
 ```
**Result:**
```python
   ModeResult(mode=array([86]), count=array([3]))

   ##The mode() method returns a ModeResult object that contains the mode number (86), and count (how many times the mode number appeared (3)).
```

## Standard Deviation (σ)
* Standard deviation is a number that describes how spread out the values are.
* A low standard deviation means that most of the numbers are close to the mean (average) value.
* A high standard deviation means that the values are spread out over a wider range.
> Use the NumPy **std()** method to find the standard deviation:
   
```python
   import numpy
   speed = [86,87,88,86,87,85,86]
   x = numpy.std(speed)
   print(x)
   
   speed1 = [32,111,138,28,59,77,97]
   y = numpy.std(speed1)
   print(y)
```
**Result:**
```python
   0.9035079029052513
   
   37.84501153334721
```

![Congrats](https://previews.123rf.com/images/hydognik/hydognik1105/hydognik110500031/9599271-hand-shake-with-a-congratulation.jpg)

# Hooray, Congratulations You finished this module now you know the basics of NumPy..:smile:
# Kudos on the Achievement..
## If you really developed an interest in NumPy and want dive deep into it, check out the resources below.....
* [NumPy](https://numpy.org/devdocs/user/absolute_beginners.html)
* [W3schools](https://www.w3schools.com/python/numpy_intro.asp)
* [GeeksforGeeks](https://www.geeksforgeeks.org/python-numpy/)


**Contributor: MUTUKUNDU MAHENDRA REDDY**

You can reach me on my mail at ***reddymahendra52@gmail.com.***


   
   
  
  

