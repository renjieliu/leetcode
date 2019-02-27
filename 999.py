def numRookCaptures(board: 'List[List[str]]'):
    #locate the Rook
    for i in range(0, 8):
        for j in range(0,8):
            if board[i][j] == "R":
                pos = [i,j]

    total = 0
    # look left
    for k in range(pos[1], -1, -1):
        if board[pos[0]][k] == "B":
            break
        if board[pos[0]][k] == "p":
            total+=1
            break

    # look right
    for k in range(pos[1], 8):
        if board[pos[0]][k] == "B":
            break
        if board[pos[0]][k] == "p":
            total+=1
            break


    #look up

    for k in range(pos[0], -1, -1):
        if board[k][pos[1]] == "B":
            break
        if board[k][pos[1]] == "p":
            total+=1
            break


    #look down

    for k in range(pos[0], 8):
        if board[k][pos[1]] == "B":
            break
        if board[k][pos[1]] == "p":
            total+=1
            break

    return total

print(numRookCaptures( [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))
print(numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
print(numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
