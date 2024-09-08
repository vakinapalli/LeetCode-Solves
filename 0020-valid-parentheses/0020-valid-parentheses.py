class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        for i in range(len(s)):
            if s[i] in ('(', '[', '{'):
                stack.append(s[i])
            elif not stack:
                return False
            elif s[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[i] == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s[i] == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
                        