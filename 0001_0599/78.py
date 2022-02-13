class Solution:
    def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
        def combo(output, curr, v, arr): #find all the combinations of the length v.
            if len(curr) == v :
                output.append(curr) 
            else:
                for i in range(len(arr)):
                    combo(output, curr + [arr[i]], v, arr[i+1:])
        output = []
        for v in range(len(nums)+1):
            combo(output, [], v, nums)
        return output

    

# previous approach

# class Solution:
#     def subsets(self, nums: 'List[int]') -> 'List[List[int]]':
#         def combo(output, curr, target, arr):
#             if len(curr) == target:
#                 output.append(curr)
#             else:
#                 for i in range(len(arr)):
#                     combo(output, curr+[arr[i]], target, arr[i+1:])
#         output = [[]]
#         for k in range(1, len(nums)+1):
#             for i, n in enumerate(nums):
#                 combo(output, [n], k, nums[i+1:])
#         return output


# previous approach

# class Solution:
    
#     def combo(self, n, k):
#         if len(n)<=k:
#             return [n]

#         else:
#             output = []
#             for i in range(len(n)):
#                 rest = n[:i]+n[i+1:]

#                 for x in self.combo(rest,k):
#                     output.append(x)

#         result = []
#         for i in output:
#             if i not in result:
#                 result.append(i)

#         return result
    
    
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         output = []
#         for i in range(1, len(nums)+1):
#             for x in self.combo(nums, i):
#                 output.append(x)
#         output.append([])
#         return output

