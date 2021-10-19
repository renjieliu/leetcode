class Solution:
    def numberOfArithmeticSlices(self, A: 'List[int]') -> int:
        if len(A) < 3: return 0
        l = 0
        r = 1
        cnt = 0
        currDiff = A[r] - A[l]
        while r < len(A):
            if A[r] - A[r-1] != currDiff:
                length = r-1 -l+1
                cnt += 0 if length < 3 else (1+length-2) * (length-2)//2 #3-->1, 4-->2...sum = (1+n)*n//2
                currDiff = A[r] - A[r-1]
                l = r-1
            r+=1
        length = r-1 -l+1
        cnt += 0 if length < 3 else (1+length-2) * (length-2)//2 #3-->1, 4-->2...sum = (1+n)*n//2

        return cnt






