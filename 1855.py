class Solution:
    def maxDistance(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
        def binFind(arr, v, pos): #find the last one larger than v
            s = pos
            e = len(arr)-1
            output = -1
            while s <= e:
                mid = s - (s-e)//2
                if arr[mid] >= v:
                    output = mid
                    s = mid + 1
                else:
                    e = mid - 1
            return output
        # hmp = {}
        # for i, n in enumerate(nums2):
        #     if n not in hmp:
        #         hmp[n] = []
        #     hmp[n].append(i)
        output = 0
        for i, n in enumerate(nums1): # for each num, find the last larger number in nums2, with pos >=i
            pos = binFind(nums2, n, i)
            if pos != -1:
                output = max(output, pos-i)

        return output