class Solution:
    def sumOfUnique(self, nums: 'List[int]') -> int:
        hmp={}
        output = 0
        for n in nums:
            if n not in hmp:
                hmp[n] =0
            hmp[n] +=1
        for k, v in hmp.items():
            output += k if v == 1 else 0
        return output