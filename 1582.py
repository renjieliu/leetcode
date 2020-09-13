class Solution:
    def numSpecial(self, mat: 'List[List[int]]') -> int:
        r_1 = {}
        c_1 = {}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    if r not in r_1:
                        r_1[r] = 0
                    r_1[r] += 1
                    if c not in c_1:
                        c_1[c] = 0
                    c_1[c] += 1
        output = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1 and r_1[r] == 1 and c_1[c] == 1:
                    output += 1
        return output


