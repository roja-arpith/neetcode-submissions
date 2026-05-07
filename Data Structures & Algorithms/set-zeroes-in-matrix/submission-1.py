class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])

        zero_first_row = False
        zero_first_col = False

        for i in range(cols):
            if matrix[0][i] == 0:
                zero_first_row = True
        
        for i in range(rows):
            if matrix[i][0] == 0:
                zero_first_col = True

        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1,rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if zero_first_row:
            for i in range(cols):
                matrix[0][i] = 0
        
        if zero_first_col:
            for i in range(rows):
                matrix[i][0] = 0
        