class Solution:
    def pivotInteger(self, n: int) -> int: # O( logN | 1 )
        s = 1 
        e = n 
        while s <= e:
            mid = s - (s-e)//2 
            curr = (1 + mid) * mid // 2
            rest = (mid + n) * (n-mid+1)//2 #sum from from mid to n 
            if curr == rest: # found the pivot point
                return mid
            elif curr < rest:
                s = mid + 1
            else:
                e = mid - 1
        
        return -1


