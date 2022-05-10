class Solution:
    def combinationSum3(self, k: int, n: int) -> 'List[List[int]]': # O( (9!k // (9-k)!) | N) --> Time: C(9, K), Space (N)
        def helper(output, total, curr, k, n, arr): #dfs to find all the combinations and add to the output
            if total == n and len(curr) == k:
                output.append(curr)
            elif total < n and len(curr) < k: # if total is larger than the target or curr has more elements, no need to continue
                for i in range(len(arr)):
                    helper(output, total + arr[i], curr + [arr[i]], k, n, arr[i+1:])
        output = []
        helper(output, 0, [], k, n, list(range(1, 10)))
        return output
    


# previous solution

# class Solution:
#     def combinationSum3(self, k: int, n: int) -> 'List[List[int]]':
#         if n<k: return []
#         arr = [_ for _ in range(1, 10)]
#         def combo(target, val, arr, output, curr):
#             if len(curr) > target:
#                 return None
#             elif len(curr) == target:
#                 t = sum(curr)
#                 if t == val:
#                     output.append(curr)
#                 elif t>val:
#                     return -1
#             else:
#                 for i in range(len(arr)):
#                     if combo(target, val, arr[i+1:], output, curr + [arr[i]]) == -1:
#                         break 
        
#         output = []
#         combo(k, n, arr, output, [])
#         return output


# previous solution

# class Solution:
#     def combinationSum3(self, k: int, n: int) -> 'List[List[int]]':
#         if n<k: return []
#         arr = [_ for _ in range(1, 10)]
#         def combo(target, val, arr, output, curr):
#             if len(curr) > target:
#                 return None
#             elif len(curr) == target:
#                 t = sum(curr)
#                 if t == val:
#                     output.append( sorted(curr) )
#                 elif t>val:
#                     return -1
#             else:
#                 for i in range(len(arr)):
#                     if combo(target, val, arr[:i] + arr[i+1:], output, curr + [arr[i]]) == -1:
#                         break 
        
#         output = []
#         combo(k, n, arr, output, [])
        
#         hmp = {}
#         for item in output:
#             if tuple(item) not in hmp:
#                 hmp[tuple(item)] = None

#         return [list(k) for k in hmp.keys()]
            



# previous solution

# def combinationSum3(k: int, n: int):
#     def dfs(output, curr_arr, candidates,target,target_len, curr_index):
#         if sum(curr_arr) ==target and len(curr_arr)==target_len:
#             output.append(curr_arr.copy())
#             return -1

#         for i in range(curr_index, len(candidates)):
#             if len(curr_arr) >= target_len or sum(curr_arr) > target:
#                 break

#             curr_arr.append(candidates[i])
#             _ = dfs(output,curr_arr, candidates, target, target_len, i+1)
#             curr_arr.pop()

#         return -1


#     if n <= 0:
#         return []
#     else:
#         output = []
#         _ = dfs(output,[], range(1,10), n, k, 0)
#         return output

# print(combinationSum3(3,7))
# print(combinationSum3(3,9))