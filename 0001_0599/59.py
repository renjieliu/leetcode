class Solution:
    def generateMatrix(self, n: int) -> 'List[List[int]]':
        arr = [_ for _ in range(1, n**2+1)]
        output = [[None for _ in range(n)] for _ in range(n)]
        r = c = 0
        direct = 0 #direction 0,1,2,3 -right, down, left, up
        while arr:
            if direct == 0:
                if output[r][c]!= None: c+=1
                while c<n and output[r][c] == None:
                    output[r][c] = arr.pop(0)
                    c+=1
                if c>=n or output[r][c] != None: c-=1
                direct = 1
            if direct == 1:
                if output[r][c]!= None: r+=1
                while r < n and output[r][c] == None:
                    output[r][c] = arr.pop(0)
                    r+=1
                if r>=n or output[r][c] != None: r-=1
                direct = 2
            if direct == 2:
                if output[r][c]!= None: c-=1
                while c > -1 and output[r][c] == None:
                    output[r][c] = arr.pop(0)
                    c-=1
                if c<=-1 or output[r][c] != None: c+=1
                direct = 3
            if direct == 3:
                if output[r][c]!= None: r-=1
                while r > -1 and output[r][c] == None:
                    output[r][c] = arr.pop(0)
                    r-=1
                if r<=-1 or output[r][c] != None: r+=1
                direct = 0
        return output
