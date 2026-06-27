# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = ptr = ListNode() # create node and two pointers (1 - start of list, 2 - iterator)

        # iterate over both lists (conditional will prevent run on empty list)
        # zip tg based on value size
        while list1 and list2:
            if list1.val < list2.val:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next
            ptr = ptr.next

        ptr.next = list1 or list2 # conditional will

        return start.next # returns actual start of list and not dummy node


