class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        op = {"+":operator.add,
              "-":operator.sub,
              "*":operator.mul,
              "/":operator.floordiv}

        stack = []

        for i in tokens:
            if i not in ("+", "-", "/", "*"):
                stack.append(i)
            else:
                operation = op[i]
                a = int(stack.pop())
                b = int(stack.pop())
                if operation == operator.floordiv and a * b < 0:
                    stack.append(operation(abs(b), abs(a)) * -1)
                else:
                    stack.append(operation(b,a))
                #print(stack[-1])
        return int(stack[-1])

