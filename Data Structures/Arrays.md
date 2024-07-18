An Array is a contiguous data structure, this means that the array is stored in blocks of memory that are right beside each other with no gaps.

![[Pasted image 20240717000219.png]]

The advantage of doing this is that retrieving values is very easy.

Depending on the language, arrays can be homogeneous, containing the same type of value (like in Java) or heterogeneous containing multiple kinds of data (like in Python)

#### Common Operations on Arrays
- Access and read values
- Search for an arbitrary values
- Insert values at any point into the structure
- Delete values in the structure

In Python when we are appending items to one list, if the element that we are allocation on the array exceeds the list's size then Python uses an Resize algorithm but this only happens in certain sizes, this re-size pattern follows the next growth pattern: 0,4,8,16,25,35, 46 an so on.

This means that as the list size approaches this specific values, resize is called again. So the append operation has a Amortized Constant Space Complexity.

*This also happens with the Insert operation.*
