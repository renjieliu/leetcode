class Solution:
    def averageValue(self, nums: 'List[int]') -> int: # O( N | 1 )
        total = cnt = 0
        for n in nums: # go through all the numbers, and get the ones satisfy the condition
            cnt += 1 if n%6 == 0 else 0
            total += n if n%6 == 0 else 0
        return 0 if cnt == 0 else total // cnt

