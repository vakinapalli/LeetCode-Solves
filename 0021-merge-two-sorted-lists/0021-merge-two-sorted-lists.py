# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        
        a = ListNode()
        a = list1
        b = list2
        ans = list2
        while a != None and b != None:
            if a.val >= b.val:
                if b.next == None:
                    b.next = a
                    break
                else:
                    temp = b
                    while temp.next.val < a.val:
                        
                        temp = temp.next
                        if temp == None or temp.next == None:
                            break
                    hold = a.next
                    a.next = temp.next
                    temp.next = a
                    a = hold
            elif a.val < b.val:
                ans = list1
                temp = a.next
                a.next = b
                b = a
                a = temp
        
        return ans
        

