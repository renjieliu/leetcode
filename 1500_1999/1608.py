class Solution:
    def specialArray(self, nums: 'List[int]') -> int:
        def compare(v, arr):
            output = 0
            for a in arr:
                output += 1 if a >= v else 0
            return output

        for i in range(1, len(nums) + 1):
            if compare(i, nums) == i:
                return i
        return -1
