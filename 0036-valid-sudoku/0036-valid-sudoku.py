class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        blocks = [ [set() for _ in range(3)] for _ in range(3)]

        for i,row in enumerate(board):
            for j,elem in enumerate(row):
                if elem != '.':
                    if elem in rows[i] or elem in cols[j] or elem in blocks[int(ceil((i+1)/3.0)-1)][int(ceil((j+1)/3.0)-1)]:

                        return False
                    rows[i].add(elem)
                    cols[j].add(elem)
                    blocks[int(ceil((i+1)/3.0)-1)][int(ceil((j+1)/3.0)-1)].add(elem)
        return True

        

        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        