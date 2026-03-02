# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse_list(head: Optional[ListNode]) -> None:
            prev = None
            curr = head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

        """
        can use slow and fast ptrs to find middle of list
        works bcz fast ptr has traveled 2x distance of the slow ptr
        so when it reaches the end, slow ptr is at the middle
        """

        # get length of list
        n = 1 if head else 0
        end = head
        while end and end.next:
            n += 1
            end = end.next
        
        # get midpoint - 1
        second = head
        for _ in range(ceil(n/2) - 1):
            second = second.next

        # split into two        
        temp = second.next
        second.next = None
        second = temp

        reverse_list(second)

        start = head
        for _ in range(n//2):
            temp1 = start.next
            temp2 = end.next
            
            start.next = end
            end.next = temp1

            start = temp1
            end = temp2
            









        


