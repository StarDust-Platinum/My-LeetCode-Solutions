class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = []
        c = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='X':
                    res.append((i,j))
                    if (i-1, j) not in res and (i, j-1) not in res:
                        c += 1
        return c