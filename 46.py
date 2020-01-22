class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        def perm(output, curr, pool, target_length):
            if len(curr) == target_length:
                output.append(curr)
                return 0
            i = 0
            while i < len(pool):
                t =  curr+[pool[i]]
                perm(output,t, pool[:i]+ pool[i+1:], target_length)
                i+=1
        output = []
        perm(output, [], nums, len(nums))
        return output