class Solution:
    def diagonalSort(self, mat: 'List[List[int]]') -> 'List[List[int]]':
        check = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]  # to see if current cell has been sorted
        r = 0
        while r < len(mat):  # go thru each cell, and find the next cells. sort them and put them back
            c = 0
            while c < len(mat[0]):
                if check[r][c] == 0:
                    temp_co = []
                    temp_value = []
                    sr = r
                    sc = c
                    while sr < len(mat) and sc < len(mat[0]):
                        temp_co.append([sr, sc])
                        temp_value.append(mat[sr][sc])
                        check[sr][sc] = 1
                        sr += 1
                        sc += 1
                    temp_value.sort()
                    i = 0
                    while i < len(temp_value):
                        mat[temp_co[i][0]][temp_co[i][1]] = temp_value[i]
                        i += 1
                c += 1
            r += 1
        return mat
