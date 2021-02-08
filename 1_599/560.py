class Solution:
    def subarraySum(self, nums: 'List[int]', k: int) -> int:
        hmp = {0:1}
        output = 0
        s = 0
        for n in nums:
            s+=n
            if s-k in hmp:
                output+=hmp[s-k]
            if s not in hmp:
                hmp[s] = 0
            hmp[s]+=1
        return output
