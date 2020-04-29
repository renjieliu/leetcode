class Solution:
    def searchRange(self, nums: 'List[int]', target: int) -> 'List[int]':
        l = float('inf')
        r = -float('inf')
        s = 0
        e = len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:  # found, and keep searching on the left
                l = min(l, mid)
                r = max(r, mid)
                s = mid + 1
            elif nums[mid] < target:
                s = mid + 1
            elif nums[mid] > target:
                e = mid - 1
        s = 0
        e = len(nums) - 1
        while s <= e:
            mid = (s + e) // 2
            if nums[mid] == target:  # found, and keep searching on the right
                l = min(l, mid)
                r = max(r, mid)
                e = mid - 1
            elif nums[mid] < target:
                s = mid + 1
            elif nums[mid] > target:
                e = mid - 1

        return [l, r] if l != float('inf') else [-1, -1]


