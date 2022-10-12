class Solution:
    def largestPerimeter(self, nums: 'List[int]') -> int: # O( NlogN | 1 )
        nums.sort()
        for i in range(len(nums)-3, -1, -1):  #greedy to find the triplets.
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


    


# previous solution

# def largestPerimeter(A: 'List[int]'):
#     pool =A
#     pool.sort()
#     for i in range(len(A)-1, 1, -1):
#         if pool[i] + pool[i-1]  > pool[i-2]  \
#                 and pool[i]+ pool[i-2] > pool[i-1]  \
#                 and pool[i-2]+ pool[i-1] > pool[i] :
#                 #and pool[i] + pool[i-1]+pool[i-2] > max:

#             return pool[i] + pool[i-1]+pool[i-2]


#     return 0

# #print(combo([18,2,7,15,14,1],3))

# print(largestPerimeter( [3,6,2,3]))
# print(largestPerimeter( [3,2,3,4]))
# print(largestPerimeter( [2,1,2]))
# print(largestPerimeter( [1,2,1]))
# print(largestPerimeter( [18,2,7,15,14,1,40,147,85,16,31])) #89
# print(largestPerimeter( [8,20,34,74,23,20,8,32,46,13,46,22,41,16,35,38,199,45,12,46,3,19,11,31,25,46,28,6,20,13,12])) #89



