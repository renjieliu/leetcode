class Solution:
    def findLength(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
        def valid(arr1, arr2, v):
            combo = set()
            for i in range(len(nums2)+1-v):
                combo.add(tuple(nums2[i:i+v]))

            for i in range(len(nums1)):
                if tuple(nums1[i:i+v]) in combo:
                    return True
            return False


        s = 0
        e = len(nums1)
        ans = 0
        while s <= e: # binary search to find the arr length which is valid for both lists
            mid = (s+e)//2
            if valid(nums1, nums2, mid):
                ans = max(ans, mid)
                s = mid +1
            else:
                e = mid -1

        return ans




