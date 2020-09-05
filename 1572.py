class Solution:
    def diagonalSum(self, mat: 'List[List[int]]') -> int:
        output = 0
        for i in range(len(mat)) : #diag1
            output+= mat[i][i]
        for i in range(len(mat)-1, -1 , 0-1): #diag2
            output+=mat[i][len(mat)-1-i]
        mid = len(mat)//2
        # deduct the cross point, which has been added twice, if the length is an even number, there's no cross point
        return output if len(mat)% 2 == 0 else output - mat[mid][mid]

