class Solution:
    def maxDistance(self, colors: 'List[int]') -> int:    
        def helper(arr) :
            for i in range(len(arr)-1, -1, -1): #find the last one different from arr[0]
                if arr[i] != arr[0]:
                    return i
        return max(helper(colors), helper(colors[::-1])) #using a[0] as base, or using a[-1] as base  


# previous approach: #O(N2)
# class Solution:
#     def maxDistance(self, colors: 'List[int]') -> int: 
#         output = -float('inf')
#         for i in range(len(colors)):
#             for j in range(len(colors)):
#                 if colors[i] != colors[j]:
#                     output=max(output, j-i)
#         return output
            
