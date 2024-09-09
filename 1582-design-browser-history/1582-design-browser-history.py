class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.past = [homepage]
        self.future = []
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.past.append(url)
        del self.future[:]
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps + 1 > len(self.past):
            steps = len(self.past) - 1

        for i in range(steps):
            self.future.append(self.past[-1])
            self.past.pop()
        return self.past[-1]       

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if not self.future:
            return self.past[-1]
        if steps > len(self.future):
            steps = len(self.future) 

        for i in range(steps):
            self.past.append(self.future[-1])
            self.future.pop()
        return self.past[-1]       

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)