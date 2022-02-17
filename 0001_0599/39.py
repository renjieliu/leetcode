class Solution:
    def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
        def helper(output, target, arr, curr, currTotal): #find the combination sumed up to target, same approach as to find all combinations
            if currTotal == target:
                output.append(curr)
            elif currTotal < target:
                for i in range(len(arr)): #pass the arr from i, to avoid duplicates combination with the previous
                    helper(output, target, arr[i:], curr + [arr[i]], currTotal + arr[i])
        
        # candidates.sort() # no need to sort. as the combination is independent on the order.
        output = []
        helper(output, target, candidates, [], 0)
        return output
    
    

# previous approach

# class Solution:
#     def combinationSum(self, candidates: 'List[int]', target: int) -> 'List[List[int]]':
#         candidates.sort()

#         def helper(output, curr, target, arr):
#             if target == 0:
#                 output.append(curr)
#             for i in range(len(arr)):
#                 if arr[i] <= target:
#                     helper(output, curr + [arr[i]], target - arr[i], arr[i:])
#                 else:
#                     break

#         output = []
#         helper(output, [], target, candidates)
#         return output

#previous solution
# def combinationSum(candidates: 'List[int]', target: int):
#     def dfs(output, curr, candidates, target, currIndex = 0 ):
#         if sum(curr) == target:
#             output.append(curr.copy())
#             return 1
#
#         for i in range(currIndex, len(candidates)):
#             if sum(curr) > target:
#                 break
#             curr.append(candidates[i])
#             x = dfs(output, curr, candidates, target, i)
#             curr.pop()
#
#
#     output = []
#     curr = []
#     candidates.sort()
#
#     if candidates == []:
#         return []
#
#     dummy = dfs(output, curr, candidates, target, 0) #main, calling the function.
#
#
#     return output
#
# print(combinationSum(candidates = [2,3,6,7], target = 7))
# print(combinationSum(candidates = [2,3,5], target = 8))

