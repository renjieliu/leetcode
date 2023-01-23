class Solution:
    def getCommon(self, nums1: 'List[int]', nums2: 'List[int]') -> int: # O( NlogN | 1 )
        def binFind(arr, v): # to check if v is in arr
            if v < arr[0] or v > arr[-1]:
                return False 
            else:
                s = 0 
                e = len(arr)-1
                while s <= e:
                    mid = s - (s-e)//2
                    if arr[mid] == v:
                        return True 
                    elif arr[mid] > v:
                        e = mid - 1
                    else:
                        s = mid + 1 
                return False 
        
        for n in nums1: 
            if binFind(nums2, n):
                return n
        return -1  # does not find 
    
    
