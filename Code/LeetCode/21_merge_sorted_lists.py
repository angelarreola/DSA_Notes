class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        d = ListNode(0)
        cur = d
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        cur.next = list1 if list1 else list2
        return d.next

def build_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
    return head

def print_list(head):
    while head:
        print(f"{head.val} -> ", end="")
        head = head.next
    print("")
        


list1 = [1,2,4]
list2 = [1,3,4]

head1 = build_linked_list(list1)
head2 = build_linked_list(list2)

print_list(head1)
print_list(head2)

solution = Solution()
result = solution.mergeTwoLists(head1, head2)

print_list(result)
