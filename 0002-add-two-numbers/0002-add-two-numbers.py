# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        hl1 = l1
        hl2 = l2
        b1 = l1
        b2 = l2
        while l1 and l2:
            a = l1.val + l2.val + carry
            carry = 0
            l1.val = l2.val = a % 10
            if a > 9:
                carry = 1
            b1 = l1
            b2 = l2
            l1 = l1.next
            l2 = l2.next

        ans = hl2
        go = None
        if l1 and not l2:
            b2.next = l1
            ans = hl2
            go = l1
        elif l2 and not l1:
            b1.next = l2
            ans = hl1
            go = l2
        elif not l2 and not l1 and carry:
            b2.next = ListNode(1)
        
        while go:
            go.val = sume = go.val + carry
            if sume == 10:
                go.val = 0
            else:
                break
            if sume == 10 and go.next == None:
                go.next = ListNode(1)
                break
            go = go.next
        

        return ans
        

                