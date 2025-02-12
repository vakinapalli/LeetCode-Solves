class Solution:

    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        hold = []
    

        def bt(ph, it, tar):
            #print(tar, " ", ph)
            if tar == 0 and ph not in ans:
                #print(ph)
                ans.append(list(ph))
            elif tar < 0:
                return
            else:
                ad = list(ph)
                for i in range(it, len(candidates)):
                    ad.append(candidates[i])
                    for j in range(i, len(candidates)):
                        bt(ad, j, tar - candidates[i])
                    ad.pop()
        bt(hold, 0, target)
        return ans
