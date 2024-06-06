class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for string in strs:
            freqmap = [0 for x in range(26)]
            for let in string:
                freqmap[ord(let) - ord("a")] += 1
            if tuple(freqmap) in dic:
                dic[tuple(freqmap)].append(string)
            else:
                dic[tuple(freqmap)] = [string]
        return [dic[x] for x in dic]


        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        