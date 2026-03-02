# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums_one = []
        nums_two = []

        while l1:
            nums_one.append(l1.val)
            l1 = l1.next
        
        while l2:
            nums_two.append(l2.val)
            l2 = l2.next
        
        nums_one.reverse()
        nums_two.reverse()

        num1 = 0
        for n in nums_one:
            num1 = num1 * 10 + n
        
        num2 = 0
        for n in nums_two:
            num2 = num2 * 10 + n

        total = num1 + num2
        digits = [int(d) for d in str(total)][::-1]

        head = ListNode()
        curr = head
        n = len(digits)
        for i in range(n):
            curr.next = ListNode(digits[i], None)
            curr = curr.next
        
        return head.next
