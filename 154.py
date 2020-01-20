class Solution:
    def findMin(self, nums: 'List[int]') -> int:
        def find(arr, ref):  # in the arr, to find a number smaller than the ref
            if len(arr) == 0:
                return float('inf')
            s = 0
            e = len(arr) - 1
            t = float('inf')
            while s <= e:
                mid = (s + e) // 2
                if arr[mid] < ref:
                    t = arr[mid]
                    e = mid - 1
                elif arr[mid] > ref:
                    s = mid + 1
                elif arr[mid] == ref:
                    l = find(arr[:mid], ref)  # to find in left, if not found, it becomes float('inf')
                    r = find(arr[mid + 1:], ref)  # to find in the right part, if not found it becomes float('inf')
                    return min(l, r)
            return t  # if not found it becomes float('inf')

        return min(find(nums, nums[0]), nums[0])