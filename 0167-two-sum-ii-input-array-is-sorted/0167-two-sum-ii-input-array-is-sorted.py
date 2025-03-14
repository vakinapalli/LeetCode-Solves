class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b= len(numbers) - 1

        while a != b:
            if numbers[a] + numbers[b] == target:
                return [a + 1, b+ 1]
            if numbers[a] + numbers[b] > target:
                b = b - 1
            else:
                a = a + 1   