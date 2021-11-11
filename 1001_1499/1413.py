class Solution:
    def minStartValue(self, nums: 'List[int]') -> int:
        mi = nums[0] # find the min accu sum in the nums
        curr = mi
        for n in nums[1:]:
            curr+=n 
            if curr < mi:
                mi = curr
        return 1 if mi >= 1 else abs(mi) + 1 
    



# previous approach
# class Solution:
#     def minStartValue(self, nums: 'List[int]') -> int:
#         i = 1
#         while True:
#             s = i
#             err = 0
#             for n in nums:
#                 s += n
#                 if s < 1:
#                     err =1
#                     break
#             if err == 0:
#                 return i
#             i+=1