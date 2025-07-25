** is the exponent / power symbol  2**4 = 2^4
// integer division symbol
* used with string results in string replication 
str * str doesn't exist
str * float doesn't exist
'' takes precendence over "" 
str needs explicit conversion 
str(29) = the characters "29" 

int() function is used to turn string integers to normal integers or to round off floats

str() is used to turn normal integers to string integers

i can simply use while True/1 for an infinite loop

CTRL+C is a keyboard interrupt error that can be used to stop infinite loop 

empty string is also treated as false. 

range(start point, end point, step argument)

from "Module" import * syntax can be used as using namespace

use global keyword to specify global scope of a variable with same names. 


- In Python, variables never contain values. They contain only references to values.
   
- In Python, the = assignment operator copies only references. It never copies values.


LIST- 
- works same as arrays in terms of accessing elements [0],[1]etc
- in case of multiple lists in the same container (somewhat like a 2d matrix) the index refers to [list number] [element number from the selected list]
- negative indices are allowed where [-1] is the last element and [-2] moves back 1 space so on and so forth
- data can be accesssed in slices 
1:3 means from the first element to the thrid element 
- in slices the first element number is included and the last element number is excluded
-concatenation and replication works in the same way. 
-del keyword can be used to delete an element
- 'in' keyword to check whether an element is present in a list
-multiple vairables can be initialized with their respective(respective to order) elements from the list on the condition that the number of elements and the number of variables must be the same. (otherwise error)
- enumerate function can be used to return 2 values, the index of the element and the element itself.
- lists are vectors and are created using []
- tuples are arrays and are created using ()
-list and tuples are interconvertible by using the keyword tuple(list)-> turns list into a tuple and vice versa

- methods are inbuilt functions
    - .append() to add elements at the end
    - .insert(index, element)
    - .remove() to remove the said element
    - sort() to sort the list numerically or ASCIIbetical (alphabetical) 
        - reverse = True to reverse sort order
        - can't sort a list with both numbers and strings. 
        - Uppercase takes priority over all lowercase due to order
            - .sort(key=str.lower) for true alphabetical order  
    - .reverse() to reverse the list
- '/' is considered as the continuation character in py code.
- with and statements if the first condition is not true the second condition is not even checked. 

by default, ALL LISTS PASS BY REFERNCE IN PYTHON. 
    


