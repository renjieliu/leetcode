class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> int: # O( N | 1 )
        l = len(nums) # pointer for the first slot can be used. Initialize l = len(nums), in case no dups in the array
        r = 1 # pointer to go through the arr 
        while r < len(nums):
            if nums[r] == nums[r-1]:
                if l == len(nums):
                    l = r 
            elif l != len(nums): # current is not the same as the previous one, move it to the first available slot
                nums[l] = nums[r]
                l += 1
            r += 1 
        return l
                

        


# previous solution

# def removeDuplicates(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     i = 1
#     while i<len(nums):
#         if nums[i]==nums[i-1]:
#             nums.pop(i)
#             i-=1
#         i+=1
#     # print(nums)
#     return len(nums)

# print(removeDuplicates([1,1,2]))
# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))