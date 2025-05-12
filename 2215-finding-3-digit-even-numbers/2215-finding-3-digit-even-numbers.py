class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq_map = dict()
        ans = []
        for i in digits:
            freq_map[i] = freq_map.get(i, 0) + 1 
        free = [0 for i in range(0,10)]
        for i in range(1,10):
            free[i]+=1
            for j in range(0,10):
                free[j]+=1
                for k in range(0,10,2):
                    free[k]+=1
                    if freq_map.get(i,0) >= free[i] and freq_map.get(j,0) >=free[j] and freq_map.get(k,0) >= free[k]:
                        ans.append((i * 100) + (j * 10) + k)
                    free[k]-=1
                free[j]-=1
            free[i]-=1
                    
        return ans
            
            
            