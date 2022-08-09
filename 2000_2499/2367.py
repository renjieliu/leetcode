class Solution:
    def arithmeticTriplets(self, nums: 'List[int]', diff: int) -> int: #O( NlogN | 1 )
        def binFind(arr, start, v): #binary find in arr for v
            s = start
            e = len(arr)-1
            while s <= e:
                mid = s - (s-e)//2
                if arr[mid] == v:
                    return mid
                elif arr[mid] < v:
                    s = mid + 1 
                else:
                    e = mid - 1 
            return -1 
    
        cnt = 0 
        for i, n in enumerate(nums): # from current number, to check if curr+k and curr+2k exist in the array
            a = binFind(nums, i+1,  n+diff)  
            if a != -1:
                b = binFind(nums, a+1, n+diff*2)
                if b != -1:
                    cnt += 1
        
        return cnt
    
    

