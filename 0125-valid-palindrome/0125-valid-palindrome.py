class Solution(object):
    def isPalindrome(self, s):
        a = 0
        b = len(s) - 1
        s = s.lower()
        while a < b:

            if ord(s[a]) - ord('a') < 0 or ord(s[a]) - ord('a') > 25:
                if ord(s[a]) < 48 or ord(s[a]) > 57:
                    a += 1
                    continue
            if  ord(s[b]) - ord('a') < 0 or ord(s[b]) - ord('a') > 25:
                if ord(s[b]) < 48 or ord(s[b]) > 57:
                    b -= 1
                    continue
            if s[a] != s[b]:
                print(a, b)
                return False
            a+=1
            b-=1
        return True
        """
        :type s: str
        :rtype: bool
        """
        