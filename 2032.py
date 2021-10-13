class Solution:
    def twoOutOfThree(self, nums1: 'List[int]', nums2: 'List[int]', nums3: 'List[int]') -> 'List[int]':
        def count(hmp, arr, i):
            for a in arr:
                if a not in hmp:
                    hmp[a] = set()
                hmp[a].add(i)
        hmp = {}
        count(hmp, nums1, 1)
        count(hmp, nums2, 2)
        count(hmp, nums3, 3)
        output = []
        for k, v in hmp.items():
            if len(v) > 1:
                output.append(k)
        return output
                
