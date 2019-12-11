class Solution:
    def find132pattern(self, nums: 'List[int]') -> bool:
        if len(nums) < 3:
            return False
        minStk = [float('inf')]  # first item does not have a number on the left
        minn = float('inf')
        for i in range(1, len(nums)):
            minStk.append(min(minn, nums[i - 1]))

        stk = []
        t = -float('inf')
        for i in range(len(nums) - 1, -1, -1):
            while stk and stk[-1] < nums[i]:  # find second largest on the right
                t = stk.pop()

            if t > minStk[i]:  # this is the last popped one
                return True
            stk.append(nums[i])

        return False
