class Solution:
    def search(self, nums: 'List[int]', target: int) -> int:
        def findPivot(nums):
            if len(nums) == 1:
                return 0
            s = 0
            e = len(nums) - 1
            while s < e:
                mid = (s + e) // 2
                if nums[mid] > nums[s]:  # left array is good, check the right
                    s = mid
                else:
                    e = mid
            return s + 1  # s is the pivot point

        def bin_search(arr, t):
            s, e = 0, len(arr) - 1
            while s <= e:
                mid = (s + e) // 2
                if arr[mid] == t:
                    return mid
                elif arr[mid] > t:
                    e = mid - 1
                elif arr[mid] < t:
                    s = mid + 1
            return -1

        if nums == []: return -1

        pivot = findPivot(nums)
        if nums[-1] >= target >= nums[pivot]:
            t = bin_search(nums[pivot:],
                           target)  # search in the right part, and add the pivot to get the real index in the original array
            return -1 if t == -1 else pivot + t
        else:
            return bin_search(nums[:pivot], target)  # search in the left part.
