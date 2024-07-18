It is a linear data structure where each element in the list is contained in a separate object called a node.

A node models two pieces of information, an individual item of the data we want to store and a reference to the next node in the list.

The first node in the linked list is called the head of the list. While the last node is called the tail. This two are special.

The opposite of the head, the tail denotes the end of the list. Every node other than the tail points to the next node in the list but tails doesn't point to anything.





The list only maintains a reference to the head, although in some implementations it keeps a reference to the tails as well.

Most of the operations on the list need to be implemented quite differently compared to an array.

If an array is a train with a bunch of cars in order then a linked list is like a treasure hunt, when you start the hunt you have piece of paper with the location of the first treasure, you go to that location and you find an item along with the location to the next item of treasure, when you finally find an item that doesn't also include a location you know that the hunt has ended.

![[Pasted image 20240717000144.png]]

