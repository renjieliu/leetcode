class Solution: #O(logN)
    def findMin(self, nums: 'List[int]') -> int:
        def findPivot(arr, s, e): #smallest item location is the pivot point + 1
            if s==e:
                return -1
            else:
                mid = (s+e)//2
                if arr[mid] > arr[mid+1]:
                    return mid
                elif arr[mid] < arr[mid] +1:
                    A = findPivot(arr, s, mid)
                    if A != -1:
                        return A
                    B = findPivot(arr, mid+1, e)
                    if B != -1:
                        return B
            return -1

        pivot = findPivot(nums, 0, len(nums)-1) #if no pivot found, return the first element of the arr
        return nums[pivot+1] #if no element find, pivot is -1, -1+1 = 0, return the first element of the arr




# previous approach: O(N)
# class Solution:
#     def findMin(self, nums: 'List[int]') -> int:
#         for n in nums:  # O(n)
#             if n < nums[0]:
#                 return n
#         return nums[0]
