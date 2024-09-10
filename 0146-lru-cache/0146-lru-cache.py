class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.vals = {}
        self.lru = {}
        self.cap = capacity
        self.cur = 0

    def get(self, key):
        self.cur +=1
        """
        :type key: int
        :rtype: int
        """
        if key in self.vals:
            self.lru[key] = self.cur
            
            
            return self.vals[key]
        else: 
            return -1
        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.cur += 1
        if len(self.vals) < self.cap:
            self.vals[key] = value
            self.lru[key] = self.cur
        else:
            if key in self.vals:
                self.vals[key] = value
                self.lru[key] = self.cur
            else:
                low = 3000000
                kick = 0
            
                for ke in self.lru:
                    if self.lru[ke] < low:
                        low = self.lru[ke]
                        kick = ke
                del self.vals[kick]
                del self.lru[kick]
                
                self.vals[key] = value
                self.lru[key] = self.cur

                

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)