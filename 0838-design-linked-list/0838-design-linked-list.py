class LinkNode:
    def __init__(self):
        self.val = None
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index):
        """
        
        :type index: int
        :rtype: int
        """
        i = 0
        hold = self.head
        while hold != None:
            if i == index:
                break
            i+= 1
            hold = hold.next
        if hold:
            return hold.val
        else:
            return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.length += 1
        hold = LinkNode()
        hold.val = val
        hold.next = self.head
        self.head = hold

        if not self.tail:
            self.tail = self.head

        

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.length += 1
        hold = LinkNode()
        hold.val = val
        if self.tail:
            self.tail.next = hold
        self.tail = hold

        if not self.head:
            self.head = self.tail
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif index < self.length:
            trav = self.head
            i = 0
            while i != index - 1:
                i+= 1
                trav = trav.next
            hold = trav.next
            crea = LinkNode()
            crea.val = val
            trav.next = crea
            crea.next = hold
            self.length += 1
        

        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < self.length:
            if self.length == 1:
                self.head = self.tail = None
                self.length -= 1
            elif index == 0:
                self.head = self.head.next
                self.length -= 1
            else:
                i = 0
                trav = self.head
                while i != index-1:
                    i+=1
                    trav = trav.next
                if index == self.length - 1:
                    self.tail = trav
                trav.next = trav.next.next
                

                self.length -=1
                
                

            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)