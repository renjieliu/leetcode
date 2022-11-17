class Solution:
    def twoSumLessThanK(self, nums: 'List[int]', k: int) -> int: # O( NlogN | 1 )
        nums.sort() 
        l = 0 
        r = len(nums)-1 
        output = -1 # default to -1, as -1 is the default returned value
        while l < r: # keep moving the 2 pointers
            if nums[l] + nums[r] < k:  # compare and move the left pointer to the right
                output = max(output, nums[l] + nums[r])
                l += 1 
            elif nums[l] + nums[r] >=k: # move the right pointer to left
                r -= 1 
        
        return output




# previous solution

# class Solution:
#     def twoSumLessThanK(self, A: 'List[int]', K: int) -> int:
#         output = -1
#         for i in range(len(A)):
#             for j in range(i+1, len(A)) :
#                 if A[i] + A[j] < K:
#                     output = max(output,A[i] + A[j])
#         return output



# previous solution

# class Solution:
#     def twoSumLessThanK(self, A: 'List[int]', K: int) -> int:
#         i = 0
#         m = -float('inf')
#         while i < len(A):
#             if A[i] > K:
#                 i+=1
#                 continue
#             j = i+1
#             while j < len(A):
#                 if A[i] + A[j] < K:
#                     m = max(m, A[i] + A[j]) 
#                 j+=1
#             i+=1
#         return -1 if m==-float('inf') else m
