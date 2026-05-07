class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box_num = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                val = board[r][c]

                if val == ".":
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in box_num[box_index]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                box_num[box_index].add(val)
        
        return True