class Solution(object):
    def commonChars(self, words):
        hold = [[0] * 26 for _ in range(len(words))]

        for ind,word in enumerate(words):
            for letter in word:
                hold[ind][ord(letter) - ord('a')] += 1
        
        ans = [500] * 26
        for freqlist in hold:
            for ind,num in enumerate(freqlist):
                if num < ans[ind]:
                    ans[ind] = num
        
        final = []
        for ind,num in enumerate(ans):
            print(chr(ind + ord('a')), " :", num)
            h = [chr(ind + ord('a'))] * num
            final.extend(h)
        return final
        """
        :type words: List[str]
        :rtype: List[str]
        """
        