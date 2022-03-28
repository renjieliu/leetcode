class Solution:
    def search(self, nums: 'List[int]', target: int) -> bool: # O(logN | logN - for the recursive call)
        def binFind(arr, v):
            s = 0 
            e = len(arr)-1
            while s <= e:
                mid = s - (s-e)//2
                if arr[mid] == v:
                    return True
                elif arr[mid] > v:
                    e = mid -1
                elif arr[mid] < v:
                    s = mid + 1 
            return False 
        
        if len(nums) == 0 :
            return False
        elif len(nums) == 1:
            return nums[0] == target
        elif nums[0] >= nums[-1]: # pivot point in current array
            s = 0
            e = len(nums)-1
            mid = s - (s-e) // 2
            return self.search(nums[:mid], target) or self.search(nums[mid:], target) # search on the 1st half and 2nd.
        elif nums[0] < nums[-1]: # sorted, just do a binary search
            return binFind(nums, target)
        
    
                
# previous approach

# class Solution:
#     def search(self, nums: 'List[int]', target: int) -> bool: #O(N)
#         return target in nums 


# previous approach

# class Solution:
#     def search(self, nums: 'List[int]', target: int) -> bool:
#         def dfs(start, end, target):
#             if end - start <= 1: return target in nums[start: end + 1]
#             mid = (start + end) // 2
#             if nums[mid] > nums[end]:  # eg. 3,4,5,6,7,1,2
#                 if nums[end] < target <= nums[mid]:
#                     return dfs(start, mid, target)
#                 else:
#                     return dfs(mid + 1, end, target)
#             elif nums[mid] < nums[end]:  # eg. 6,7,1,2,3,4,5
#                 if nums[mid] < target <= nums[end]:
#                     return dfs(mid + 1, end, target)
#                 else:
#                     return dfs(start, mid, target)
#             else:
#                 return dfs(mid + 1, end, target) or dfs(start, mid, target)

#         return dfs(0, len(nums) - 1, target)

# previouos approach
# def search(nums: 'List[int]', target: int) -> bool:
#     for i in nums:
#         if i == target:
#             return True
#     return False
#
#
#
# print(search(nums = [2,5,6,0,0,1,2], target = 0))
#
# print(search(nums = [2,5,6,0,0,1,2], target = 3))




