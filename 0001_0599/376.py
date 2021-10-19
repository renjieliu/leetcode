class Solution:
    def wiggleMaxLength(self, nums: 'List[int]') -> int:
        if len(nums) == 1: return 1
        else:
            arr = []
            for i in range(1, len(nums)):
                arr.append(nums[i] - nums[i-1])
            neg = 1 if arr[0] < 0 else 0
            pos = 1 if arr[0] > 0 else 0
            for i in range(1, len(arr)): # just need to find the prev neg and pos, no need for dp array
                if arr[i] > 0:
                    pos = neg+1 #prev longest neg + 1
                elif arr[i] < 0:
                    neg = pos+1 #prev longest pos + 1
            return max(neg, pos) + 1

