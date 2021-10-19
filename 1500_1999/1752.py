class Solution:
    def check(self, nums: 'List[int]') -> bool:
        if len(nums) < 2:
            return True
        else:
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]: # find the pivot point
                    arr = nums[i:] + nums[:i] #move the elements before pivot to the end of the array
                    for j in range(len(arr)-1): # check if the new array is sorted
                        if arr[j] > arr[j+1]:
                            return False
                    return True

            return True # no pivot point found
