class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i = 0
        j = 0
        k = len(matrix) - 1
        l = len(matrix[0]) - 1
        lengthlit = len(matrix[0])

        while (i* lengthlit) + j <= k * lengthlit + l:
            mid = (((lengthlit * i) + j) + ((lengthlit*k) + l))//2 
            mii = mid // lengthlit
            mij = mid % lengthlit

            if target < matrix[mii][mij]:
                mid -= 1
                k = mid // lengthlit
                l = mid % lengthlit
            elif target > matrix[mii][mij]:
                mid += 1
                i = mid // lengthlit
                j = mid % lengthlit
            else:
                return True
        return False
