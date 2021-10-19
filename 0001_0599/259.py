class Solution:
    def threeSumSmaller(self, nums: 'List[int]', target: int) -> int:
        nums.sort()
        cnt = 0
        i = 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] >= target:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < target:
                    cnt += (k - j)
                    j += 1
            i += 1
        return cnt
