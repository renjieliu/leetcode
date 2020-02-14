class Solution:
    def twoSumLessThanK(self, A: 'List[int]', K: int) -> int:
        i = 0
        m = -float('inf')
        while i < len(A):
            if A[i] > K:
                i+=1
                continue
            j = i+1
            while j < len(A):
                if A[i] + A[j] < K:
                    m = max(m, A[i] + A[j])
                j+=1
            i+=1
        return -1 if m==-float('inf') else m
