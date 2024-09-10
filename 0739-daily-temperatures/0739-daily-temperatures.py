
class Node:
    def __init__(self, ind, val):
        self.ind = ind
        self.val = val

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(temperatures)
        a = []
        a.append(Node(0,temperatures[0]))
        for i in range(1,len(temperatures)):
            if temperatures[i] <= a[-1].val:
                a.append(Node(i,temperatures[i]))
            else:
                while a and temperatures[i] > a[-1].val:
                    hold = a.pop()
                    ans[hold.ind] = i - hold.ind
                a.append(Node(i, temperatures[i]))
        return ans



