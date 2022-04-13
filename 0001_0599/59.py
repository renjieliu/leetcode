class Solution:
    def generateMatrix(self, n: int) -> 'List[List[int]]': #O(n2 | n2)
        direction = [[0, 1], [1, 0], [0,-1], [-1, 0]]
        output = [[None for c in range(n)] for r in range(n)] 
        curr = 1 
        r, c, d = 0, 0, 0
        while curr <= n**2:
            output[r][c] = curr
            a, b = direction[d][0], direction[d][1] #next cell and value
            if r + a <= -1 or r + a >= n or c+b <= -1 or c+b >= n or output[r+a][c+b] != None: 
                d = (d+1)%4
                a, b = direction[d][0], direction[d][1]
            r += a
            c += b
            curr += 1 
        return output


# previous solution

# class Solution:
#     def generateMatrix(self, n: int) -> 'List[List[int]]':
#         arr = [_ for _ in range(1, n**2+1)]
#         output = [[None for _ in range(n)] for _ in range(n)]
#         r = c = 0
#         direct = 0 #direction 0,1,2,3 -right, down, left, up
#         while arr:
#             if direct == 0:
#                 if output[r][c]!= None: c+=1
#                 while c<n and output[r][c] == None:
#                     output[r][c] = arr.pop(0)
#                     c+=1
#                 if c>=n or output[r][c] != None: c-=1
#                 direct = 1
#             if direct == 1:
#                 if output[r][c]!= None: r+=1
#                 while r < n and output[r][c] == None:
#                     output[r][c] = arr.pop(0)
#                     r+=1
#                 if r>=n or output[r][c] != None: r-=1
#                 direct = 2
#             if direct == 2:
#                 if output[r][c]!= None: c-=1
#                 while c > -1 and output[r][c] == None:
#                     output[r][c] = arr.pop(0)
#                     c-=1
#                 if c<=-1 or output[r][c] != None: c+=1
#                 direct = 3
#             if direct == 3:
#                 if output[r][c]!= None: r-=1
#                 while r > -1 and output[r][c] == None:
#                     output[r][c] = arr.pop(0)
#                     r-=1
#                 if r<=-1 or output[r][c] != None: r+=1
#                 direct = 0
#         return output



