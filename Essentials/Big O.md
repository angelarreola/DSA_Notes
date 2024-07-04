#### Definition
Theoretical definition of the complexity of an algorithm as a function of the size.

O(n) 
- The O stands for "Order of magnitude of complexity".
- The (n) is a function of the size.
When we use Big O for measure the complexity, the variable used which we'll get to distills that information down so that by reading the variable you get a big picture view without having to run trough data points and graphs.


#### <span style="color:rgb(255, 192, 0)">O(1)</span>
Constant time, doesn't matter how big is the input, always the runtime it is going to be the same.

#### <span style="color:rgb(255, 192, 0)">O(log n)</span>
The inverse operation for an exponential it's called logarithm and this operation basically means "How many times I have to divide n by i to get one?"
- $8÷2=4$
- 4÷2=2
- $2÷2=1$
- $log_2 8 = 3$

$log_2 16 = 4$
$log_i n = x$

Look at the next example using [[Binary Search]]... If the target is 16 in a list of 16 elements, we start with the middle value which is 8. Then we discard the half of the values, and continue the same algorithm then by the end  we have 4 tries plus one that is the discard try.So we have the next formula:
$log_n + 1$

#### <span style="color:rgb(255, 192, 0)">O(</span>$n^2$<span style="color:rgb(255, 192, 0)">)</span>
For any given value of n we carry out n squared number of operations. Quadratic Runtime.
Many search algorithms have a worst case Quadratic Runtime.


#### <span style="color:rgb(255, 192, 0)">O(n log n)</span>
Quasilinear Runtimes means that for every value of n we're going to execute a log n number of operations hence the run time of n times log n. This runtime lies somewhere between a linear runtime and a quadratic runtime.

This runtime is often seen in sorting algorithms, Merge Sort as an example is an algorithm that has a worst case runtime of big o of n times log n.

#### <span style="color:rgb(255, 192, 0)">O</span><span style="color:rgb(255, 192, 0)">(</span>n^k<span style="color:rgb(255, 192, 0)">)</span>
Polynomial Runtime | For a given value of n its worst case runtime is in the form of n raised to the k power where k just means some value.

#### <span style="color:rgb(255, 192, 0)">O(</span>$X^n$<span style="color:rgb(255, 192, 0)">)</span>
Imagine that you break into a locker that had a padlock on it. 2 Digit Code, ranges from zero to nine. You try 00,01,02,....10,11,12... and then we have $10^2$ attempts, this strategy is called Brute Force.

Brute Force Algorithms have exponential runtimes.

Here there are two dials so $n = 2$ and each dial has 10 values so we can generalize this algorithm as $10^n$ where n represents the number of dials.

With 3 dials -> $10^3 = 1000$ 
With 4 dials ->  $10^4 = 10000$ 

#### <span style="color:rgb(255, 192, 0)">O(n!)</span> 
Factorial / Combinatorial
Factorials are basically n times n minus one repeated until you reach the number one.

$n! = n(n-1)(n-2)...(2)(1)$

$3! = 3*2*1 = 6$
$4! = 4*3*2*1 = 24$

At lows values of n algorithms with a factorial runtime may be used but with an n value of say 200 it would take longer than humans have been alive to solve the problem.

#### <span style="color:rgb(0, 176, 240)">Determine the Big O</span>
The algorithm has as its upper bound the same run time as the least efficient step in the algorithm 

![[Pasted image 20240704004303.png]]

