class Solution:

    def searchRow(self, matrix: list[list[int]], target: int) -> list[int]:

        r = len(matrix) - 1
        l = 0
        res = matrix[0]
        while(True):
            m = (int)((r + l) / 2)
            if l > r:
                return res
            if target == matrix[m][0]:
                return matrix[m]
            elif target > matrix[m][0]:
               l = m +1
               res = matrix[m]
            else:
               r = m-1
                

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
       
        row = self.searchRow(matrix, target)
        r = len(row) - 1
        l = 0
        while(True):
            m = (int)((r + l) / 2)
            if l >= r:
                if row[m] == target:
                    return True
                return False
            if(row[m] == target ):
                return True
            elif row[m] > target:
                r = m-1
            else:
                l = m+1

if __name__ == '__main__':
    s = Solution()
    matrix = [[1],[3]]
    target = 3
    res = s.searchMatrix(matrix, target)
    print(res)