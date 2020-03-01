class Solution:
    def findDuplicate(self, nums: 'List[int]') -> int:
        slow, fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        p = 0
        while p!=fast:
            fast = nums[fast]
            p = nums[p]
        return p