class Solution:
    def search(self, nums: 'List[int]', target: int) -> bool:
        def dfs(start, end, target):
            if end - start <= 1: return target in nums[start: end + 1]
            mid = (start + end) // 2
            if nums[mid] > nums[end]:  # eg. 3,4,5,6,7,1,2
                if nums[end] < target <= nums[mid]:
                    return dfs(start, mid, target)
                else:
                    return dfs(mid + 1, end, target)
            elif nums[mid] < nums[end]:  # eg. 6,7,1,2,3,4,5
                if nums[mid] < target <= nums[end]:
                    return dfs(mid + 1, end, target)
                else:
                    return dfs(start, mid, target)
            else:
                return dfs(mid + 1, end, target) or dfs(start, mid, target)

        return dfs(0, len(nums) - 1, target)

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




