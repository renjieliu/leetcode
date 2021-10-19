class Solution:
    def sumFourDivisors(self, nums: 'List[int]') -> int:
        def cntDivisors(n):
            temp = []
            cnt = 0
            for i in range(2, int(n**0.5)+1):
                if n%i == 0:
                    temp.append(i)
            output = []
            for t in temp:
                output.append(t)
                output.append(n//t)
            if len(set(output)) == 2:
                return output + [1, n]
            else:
                return []
        pool = []
        for i in nums:
            pool.append(cntDivisors(i))
        output = 0
        for p in pool:
            output+= sum(p)
        return output