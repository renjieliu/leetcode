class Solution:
    def maxLength(self, arr: 'List[str]') -> int: # O( 2**N | 2**N )
        def helper(output, pool, arr, curr, lvl, v): # find all the possible combo for the concat strings
            if lvl == v:
                output[0] = max(output[0], len(curr))
            else:
                for i in range(len(arr)):
                    if arr[i] & curr == set(): # all the characters are unique in the current concatenation
                        helper(output, pool, arr[i+1:], curr | arr[i], lvl+1, v)
        
        arr = [set(a) for a in arr if len(set(a)) == len(a)] #the string itself cannot have repeat characters
        output = [-float('inf')]
        for v in range(1, len(arr)+1):
            helper(output, set(), arr, set(), 0, v)
        
        return max(output[0], 0) #if none of the string is valid, return 0
    



# previous solution 

# class Solution:
#     def maxLength(self, arr: 'List[str]') -> int:
#         def combo(output, curr, nums, arr,  v): #to get all the possible combinations, and check each string
#             if len(curr) == v:
#                 tmp = ""
#                 for c in curr:
#                     tmp += arr[c]
#                 if len(set(tmp)) == len(tmp): #all uniqiue
#                     output[0] = max(output[0], len(tmp))
#             else:
#                 for i in range(len(nums)):
#                     combo(output, curr+[nums[i]], nums[i+1:], arr, v)

#         output = [0]
#         n = len(arr)
#         nums = list(range(n))
#         for i in range(n+1):
#             combo(output, [], nums, arr, i)
#         return output[0]



# previous approach
# class Solution:
#     def maxLength(self, arr: 'List[str]') -> int:
#         def findMax(curr, pos, arr):
#             if pos == len(arr):
#                 return len(curr)
#             else:
#                 A, B, C, found = 0, 0, 0, 0
#                 for c in arr[pos]:
#                     if c in curr:
#                         found = 1
#                         break
#                 if len(arr[pos]) != len(set(arr[pos])): found = 1  # dups found witin the word itself.
#
#                 if found == 0:
#                     take = curr + arr[pos]  # choose current word
#                     A = findMax(take, pos + 1, arr)
#                     B = findMax(curr, pos + 1, arr)  # skip current pos
#                 else:
#                     C = findMax(curr, pos + 1, arr)  # skip current pos
#
#                 return max(A, B, C)
#
#         i = 0
#         output = 0
#         while i < len(arr):
#             w = arr[i]
#             if len(w) != len(set(w)):
#                 i += 1
#             else:
#                 output = max(output, findMax(w, i + 1, arr))
#                 i += 1
#         return output