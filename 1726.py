class Solution:
    def tupleSameProduct(self, nums: 'List[int]') -> int:
        def combo(n, p):
            fact = lambda x: 1 if x in (0,1) else fact(x-1) * x
            return fact(n) // (fact(p)*fact(n-p))
        hmp = defaultdict(int)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j!= i:
                    curr = nums[i] * nums[j]
                    hmp[curr] +=1
        output = 0
        # print(hmp)
        for v in hmp.values():
            if v >=4: # can find a 4 digit tuple to produce the same result
                groups = v//2 #((a,b), (b,a), (c,d),(d,c)), there's only 2 real groups
                output += combo(groups,2) *8 #pick any 2 groups, and there's 8 for each 2 groups

        return output
