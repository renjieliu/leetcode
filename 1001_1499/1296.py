class Solution:
    def isPossibleDivide(nums: 'List[int]', k: int) -> bool:
        if k ==1 :
            return True
        else:
            hmp = {} 
            for n in nums:
                if n not in hmp:
                    hmp[n] = 0
                hmp[n] +=1

        while len(hmp) > 0:
            start =  min(hmp.keys())
            stk = [_  for _ in range (start ,start + k ) ]
            deduction = hmp[start]
            for s in stk:
                if s not in hmp:
                    return False 
                hmp[s] -= deduction #current number should repeat at least the same time as the first number in the stack
                if hmp[s] < 0:
                    return False
                elif hmp[s] ==0:
                    del hmp[s]
        return True