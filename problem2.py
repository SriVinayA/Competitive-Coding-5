# leetcode problem: 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Approach 1
        # time: O(1)
        # space: O(1)
        
        # # validate rows
        # for i in range(9):
        #     s = set()
        #     for j in range(9):
        #         item = board[i][j]
        #         if item != ".":
        #             if item in s:
        #                 return False
        #             else:
        #                 s.add(item)
        
        # # validate cols
        # for i in range(9):
        #     s = set()
        #     for j in range(9):
        #         item = board[j][i]
        #         if item != ".":
        #             if item in s:
        #                 return False
        #             else:
        #                 s.add(item)
        
        # # validate boxes
        # for i in range(0, 9, 3):
        #     for j in range(0, 9, 3):
        #         s = set()
        #         for row in range(i, i+3):
        #             for col in range(j, j+3):
        #                 item = board[row][col]
        #                 if item != ".":
        #                     if item in s:
        #                         return False
        #                     else:
        #                         s.add(item)
        # return True

        # Approach 2
        # time: O(1)
        # space: O(1)
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                item = board[i][j]
                if item != ".":
                    if (item in rows[i]) or (item in cols[j]) or (item in boxes[(i//3, j//3)]):
                        return False
                    else:
                        rows[i].add(item)
                        cols[j].add(item)
                        boxes[(i//3, j//3)].add(item)
        return True
