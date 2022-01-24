class Solution:
    def sequentialDigits(self, low: int, high: int) -> 'List[int]':
        def dfs(output, curr, low, high):
            if low <= curr <= high:
                output.append(curr)
            if curr % 10 < 9:
                nxt = curr*10 + curr%10+1
                dfs(output, nxt, low, high)
         
        output = []
        for i in range(1,9): #start with 1, 2,3,4.. 8. No need to calc 9.
            dfs(output, i, low, high)
        
        return sorted(output)
        



# previous approach

# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> 'List[int]':
#         def add(curr, high, output):
#             if int(curr) < high:
#                 output.append(curr)
#                 if int(curr[-1])<9:
#                     curr+= str(int(curr[-1]) + 1)
#                     add(curr, high, output)
#         output = []
#         for i in range(1, 10):
#             add(str(i), high, output)
#         res = []
#         for o in output:
#             if low <= int(o) <= high :
#                 res.append(int(o))
#         return sorted(res)


