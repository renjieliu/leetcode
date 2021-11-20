class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def less(m, n , v, k):
            cnt = 0
            for i in range(1, m+1):
                cnt += min(v//i, n) #to find how many in the current row is < v
            return cnt < k
        
        s = 1
        e = m*n
        while s <= e:
            mid = s-(s-e)//2
            if less(m,n, mid, k):
                s = mid + 1 
            else:
                e = mid - 1 
        return s
    

