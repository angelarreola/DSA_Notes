As we have seen before with the implementation of Binary Search in Python, especially the recursive solution, it has a space complexity of O(log n). But why?

This is because every iteration divides the $N$ amount of space in half, creating a new list with this divided amount. This matches the current time complexity because in every iteration we are dividing the space and time into two.

![[Pasted image 20240709183813.png]]

#### Tail Optimization
If you think of a function as having a head and a tail, and if the recursive function call is the last line of code in the function as it is in our case (the recursive solution of the binary search) we call this **Tail Recursion**, since it's the last part of the function that calls itself.

Swift uses Tail Call Optimization or Tail Call Elimination and that's why if we were using Swift we don't care about how many times the recursive function is calling at itself. But if we are using Python (as we are right now) then we need to know that Python doesn't implement anything similar to tail call optimization.

So, in python, the recursive version of binary search takes logarithmic space. Therefore, we would definitely prefer to use the iterative version since it runs in constant space.