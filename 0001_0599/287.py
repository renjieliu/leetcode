class Solution:
    def findDuplicate(self, nums: 'List[int]') -> int: # same as to find a cycle with Floyd's tortoise and hare algo
        fast = slow = nums[0]
        while True: 
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break            
        
        slow = nums[0]
        while fast!= slow:
            fast = nums[fast] 
            slow = nums[slow]
        return slow
    


# previous approach

# def findDuplicate(self, nums: 'List[int]') -> int: #Floyd's tortoise
#     h = nums[0]
#     t = nums[0]
#     while True:
#         h = nums[nums[h]]
#         t = nums[t]
#         if h == t:
#             break
#     t = nums[0]
#     while t != h:
#         t = nums[t]
#         h = nums[h]
#     return t



#OLD solution
# def findDuplicate(nums: 'List[int]'):
#     map = {}
#     for i in nums:
#         if i not in map:
#             map[i] = 1
#         else:
#             return i


# print(findDuplicate([1,3,4,2,2]))
# print(findDuplicate([1]))