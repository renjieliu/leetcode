class Solution:
    def minStartValue(self, nums: 'List[int]') -> int:
        i = 1
        while True:
            s = i
            err = 0
            for n in nums:
                s += n
                if s < 1:
                    err =1
                    break
            if err == 0:
                return i
            i+=1