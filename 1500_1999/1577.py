class Solution:
    def numTriplets(self, nums1: 'List[int]', nums2: 'List[int]') -> int:
        output = 0
        for x in [nums1, nums2]:
            compare = nums1 if x == nums2 else nums2
            hmp = {}
            for i in range(len(x)):
                for j in range(i + 1, len(x)):
                    if x[i] * x[j] not in hmp:
                        hmp[x[i] * x[j]] = 0
                    hmp[x[i] * x[j]] += 1

            for n in compare:
                if n ** 2 in hmp:
                    output += hmp[n ** 2]

        return output
