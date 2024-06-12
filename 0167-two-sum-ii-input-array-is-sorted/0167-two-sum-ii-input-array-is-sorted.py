class Solution(object):
    def twoSum(self, numbers, target):
        a = 0
        b = len(numbers) - 1

        while a < b:
            if numbers[a] + numbers[b] == target:
                return [a + 1, b + 1]
            elif numbers[a] + numbers[b] < target:
                a += 1
            else:
                b -= 1
        return []
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        