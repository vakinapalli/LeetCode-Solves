class MyStack(object):

    def __init__(self):
        self.queue = deque()
        self.count = 0
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        for i in range(self.count):
            temp = self.queue.popleft()
            self.queue.append(temp)
        self.count += 1
            

    def pop(self):
        """
        :rtype: int
        """
        self.count -=1
        return self.queue.popleft()
        

    def top(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return  not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()