class Solution:
    def decompressRLElist(self, nums: 'List[int]') -> 'List[int]':
        i = 0
        output = []
        while i < len(nums):
            if i%2 ==0:
                cnt = nums[i]
            else:
                j = 0
                while j < cnt:
                    output.append(nums[i])
                    j+=1
                cnt = 0
            i+=1
        return output