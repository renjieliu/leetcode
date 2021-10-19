class Solution:
    def minSubsequence(self, nums: 'List[int]') -> 'List[int]':
        s = sum(nums)
        stk = []
        lst = sorted(nums)
        curr = 0
        while lst and curr <= s: #take out the largest number from the array, until the curr is > than the s
            stk.append(lst.pop())
            curr += stk[-1]
            s-=stk[-1]
        return stk