class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        def dfs(output, targetLength, curr, arr):
            if len(curr) == targetLength:
                output.append(curr)
            else:
                for i in range(len(arr)):
                    dfs(output, targetLength, curr + [arr[i]], arr[:i] + arr[i + 1:])

        output = []
        dfs(output, len(nums), [], nums)
        res = []
        tp = {}
        for o in output:
            if tuple(o) not in tp:
                tp[tuple(o)] = None
                res.append(o)
        return res

# Previous approach
# class Solution:
#     def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
#         def perm(pool,curr, N, rest): #generate all the possible permutations
#             if len(curr) == N:
#                  pool.append(curr)
#             else:
#                 i=0
#                 while i < len(rest):
#                     t = curr + [rest[i]]
#                     perm(pool, t, N, rest[:i] +  rest[i+1:] )
#                     i+=1
#         pool = []
#         N = len(nums)
#         for i in range(len(nums)):
#             perm(pool, [nums[i]], N, nums[:i] + nums[i+1:])
#         hmp = {}
#         output = []
#         for p in pool: # to check if current combination is dups in the output
#             s =  '-'.join(map(lambda x:str(x), p))
#             if s not in hmp:
#                 hmp[s] = 1
#                 output.append(p)
#         return output