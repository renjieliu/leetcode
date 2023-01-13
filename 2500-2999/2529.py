class Solution:
    def maximumCount(self, nums: 'List[int]') -> int: # O( NlogN | 1 )
        def firstPos(arr): # find the first location of positive number
            if arr[-1] <= 0 :
                return len(arr) # to make total count of positive number easier
            elif arr[0] > 0:
                return 0
            else:
                s = 0 
                e = len(arr)
                output = len(arr) # to make total count of positive number easier
                while s<=e :
                    mid = s -(s-e)//2 
                    if arr[mid] > 0:
                        output = mid
                        e = mid - 1
                    else:
                        s = mid + 1
                return output
        
        def lastNeg(arr): # find the last location of negative number
            if arr[0] >= 0:
                return -1 # to make total count of negative number easier
            elif arr[-1] < 0:
                return len(arr) - 1
            else:
                s = 0 
                e = len(arr)-1
                output = -1 # to make total count of negative number easier
                while s <= e :
                    mid = s - (s-e)//2 
                    if arr[mid] < 0:
                        output = mid
                        s = mid + 1
                    else:
                        e = mid - 1
                return output
            
            
        A = len(nums)-1 - firstPos(nums) + 1 # number of positive number
        B = lastNeg(nums) + 1 # number of negative number
        
        return max(A, B)
            
            
            


# previous solution


# class Solution:
#     def maximumCount(self, nums: 'List[int]') -> int: # O( N | 1 )
#         A = B = 0
#         for n in nums: # count the positive and negative numbers in the num
#             A += n > 0 
#             B += n < 0 
#         return max(A, B)
    




