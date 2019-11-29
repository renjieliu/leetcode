class Solution:
    def shortestBridge(self, A: 'List[List[int]]') -> int:
        def fill_Island(check, A, sr, sc, island):
            if A[sr][sc] == 0 or check[sr][sc] == 1:  # or sr == len(A)-1 or sc==len(A)-1 :
                return -1  # no longer in the island
            elif A[sr][sc] == 1 and check[sr][sc] == 0:
                end = len(A)
                check[sr][sc] = 1
                island[-1].append([sr, sc])  # add to the current island
                for r in range(sr + 1, end):  # look down
                    if fill_Island(check, A, r, sc, island) == -1:
                        break
                for r in range(sr - 1, -1, -1):  # look up
                    if fill_Island(check, A, r, sc, island) == -1:
                        break
                for c in range(sc + 1, end):  # look right
                    if fill_Island(check, A, sr, c, island) == -1:
                        break
                for c in range(sc - 1, -1, -1):  # look left
                    if fill_Island(check, A, sr, c, island) == -1:
                        break
                return 1  # finish current island search

        w = len(A)
        check = [[0 for _ in range(w)] for _ in range(w)]
        island = []
        for r in range(w):
            for c in range(w):
                if A[r][c] == 1 and check[r][c] == 0:
                    island.append([])
                    fill_Island(check, A, r, c, island)
        border = [[], []]  # look on the border to determin which point need to be calculated for the manhattan distance

        i = 0
        while i < 2:
            for b in island[i]:
                if b[0] * b[1] == 0 or b[0] == w - 1 or b[1] == w - 1:
                    border[i].append(b)
                else:
                    if A[b[0] - 1][b[1]] * A[b[0] + 1][b[1]] * A[b[0]][b[1] - 1] * A[b[0]][
                        b[1] + 1] == 0:  # up #down #left #right
                        border[i].append(b)
            i += 1

        output = float('inf')
        for i in border[0]:  # find distance
            for j in border[1]:
                manhattan = abs(i[0] - j[0]) + abs(i[1] - j[1]) - 1
                output = min(manhattan, output)

        return output













