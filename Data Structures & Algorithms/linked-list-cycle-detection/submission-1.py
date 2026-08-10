# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        listO = []
        while head.next != None:
            listO.append(head.val)
            head = head.next
            if head.val in listO:
                return True
        return False
        

