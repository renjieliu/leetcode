def findKthLargest(nums: 'List[int]', k: int):
    if len(nums) == 1:
        return nums[0]

    return sorted(nums)[::-1][k - 1]



