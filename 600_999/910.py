class Solution:
    def smallestRangeII(self, A: 'List[int]', K: int) -> int:
        A = sorted(list(set(A)))
        output = A[-1] - A[0] #the worst case.
        left = A[0]+K
        right = A[-1]-K
        i = 0
        while i < len(A)-1:
            output = min(output,  max(right, A[i]+K) - min(left, A[i+1]-K)  )
            i+=1
        return output