class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # def hasCycle(self, head) -> bool:
    #     dummy = ListNode(0)
    #     dummy.next = head
    #     slow = fast = dummy
        
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
            
    #         if slow is fast:
    #             return True
            
    #     return False
    def hasCycle(self, head) -> bool:
        while head:
            if head.val == 100001:
                return True
            head.val = 100001
            head = head.next
        return False

def build_linked_list(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node

    return head

values = [3, 2, 0, -4]
pos = 1  
head = build_linked_list(values, pos)

solution = Solution()
result = solution.hasCycle(head)
print(f"¿La lista tiene ciclo? {'Sí' if result else 'No'}")

values = [1, 2]
pos = -1  
head = build_linked_list(values, pos)

result = solution.hasCycle(head)
print(f"¿La lista tiene ciclo? {'Sí' if result else 'No'}")
