"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        add2ind = dict()
        ind2add = []

        a = head
        i = 0
        dum = Node(0)
        hd = dum
        while a != None:
            add2ind[a] = i
            dum.next = Node(a.val)
            dum = dum.next
            ind2add.append(dum)
            i += 1
            a = a.next
        hd_copy = hd.next
        while hd_copy != None:
            if head.random == None:
                hd_copy.random = None
            else:
                hd_copy.random = ind2add[add2ind[head.random]]
            hd_copy = hd_copy.next
            head = head.next
        return hd.next


            
        