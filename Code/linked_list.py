"""
An object for storing a single node of a linked list.
Models two attributes - data and the link to the next node in the list
"""
class Node:
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self):
        return f"<Node: {self.data}>"

class LinkedList:
    """
    Singly Linked List
    """
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str:
        """
        Return a string representation of the list
        Takes O(n) Time
        """
        current = self.head
        nodes = []
        while current:
            if current is self.head:
                nodes.append(f"HEAD [{current.data}]")
            elif current.next_node is None:
                nodes.append(f"TAIL [{current.data}]")
            else:
                nodes.append(f"[{current.data}]")
                
            current = current.next_node
        return ' -> '.join(nodes)
    
    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list | Takes O(n) time
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node
        return count

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Takes O(1) Time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


# Alternative __rep__ of the linked list:
    # def __repr__(self) -> str:
    #     """
    #     Return a string representation of the list
    #     Takes O(n) Time
    #     """
    #     current = self.head
    #     rep = ""
    #     while current:
    #         rep += f" {current} ---> "
    #         current = current.next_node
    #     rep += "END"
    #     return rep

    