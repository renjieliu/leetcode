class Solution:
    def maxSumRangeQuery(self, nums: 'List[int]', requests: 'List[List[int]]') -> int:
        mod = 10 ** 9 + 7
        nums.sort(reverse=True)
        hmp = {_: 0 for _ in range(len(nums) + 1)}  # this is to find which element has been queried the most, 2nd ...

        for s, e in requests:  # refer to leetcode problem: 370
            hmp[s] += 1
            hmp[e + 1] -= 1
        for i in range(1, len(nums) + 1):
            hmp[i] += hmp[i - 1]
        del hmp[len(nums)]

        output = 0
        v_reverse = sorted(list(hmp.values()), reverse=True)
        # print(v_reverse)

        for v in v_reverse:
            output += nums.pop(0) * v
        return output % mod