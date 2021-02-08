def countBattleships(board: 'List[List[str]]'):
    output = 0
    for i in board:
        for j in i:
            if j == "X":
                output+=1

    for i in range(len(board)):
        s="".join(board[i])
        for x in range(len(s)-1):
            if s[x] + s[x+1] =='XX':
                output-=1

    for c in range(len(board[0])):
        s = ""
        for r in range(len(board)):
            s += board[r][c]

        for x in range(len(s) - 1):
            if s[x] + s[x + 1] == 'XX':
                output -= 1



    return output





print(countBattleships([["X",".",".","X"],
                        [".",".",".","X"],
                        [".","X",".","X"]]
                       ))


