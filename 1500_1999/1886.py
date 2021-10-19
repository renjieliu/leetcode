class Solution:
    def findRotation(self, mat: 'List[List[int]]', target: 'List[List[int]]') -> bool:
        def rotate(mat):
            output = [[None for c in range(len(mat[0]))] for r in mat]
            for r in range(len(mat)):
                for c in range(len(mat)):
                    output[r][c] = mat[c][len(mat)-1-r]
            return output
        if mat==target:
            return True
        else:
            for i in range(3):
                mat = rotate(mat)
                if mat == target:
                    return True
            return False

