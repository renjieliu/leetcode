class Solution:
    def isIdealPermutation(self, A: 'List[int]') -> bool:
        if len(A) == 1:
            return True
        else:
            local = 0
            s_arr = 0
            s_supposed = 0
            gbl = 0
            for i in range(len(A)-1, -1, -1):
                if i > 0 and A[i] < A[i-1]:
                    local += 1
                s_arr += A[i]
                s_supposed += i #current number in the sequence of [0 to N]
                delta = s_supposed - s_arr #how many diff, that's how many larger numbers are before this one.
                gbl += delta if delta > 0 else 0
                if gbl > local:
                    return False
            return gbl == local
