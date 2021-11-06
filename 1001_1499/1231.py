class Solution:
    def maximizeSweetness(self, sweetness: 'List[int]', k: int) -> int:
        def helper(arr, k, v): #to check if arr can be split into k+1 parts, with min of V value each piece
            curr = 0 
            cnt = 0
            for a in arr:
                curr+=a
                if curr >= v:
                    cnt += 1
                    curr = 0
            return cnt >= k+1 
        
        s = min(sweetness) 
        e = sum(sweetness)+1
        output = s
        while s <= e: #binary search to find the min sweetness, can be reached.
            mid = s - (s-e)//2
            if helper(sweetness, k, mid):
                output = max(mid, output)
                s = mid + 1 
            else:
                e = mid - 1 
        
        return output
    
