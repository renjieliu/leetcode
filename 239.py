def maxSlidingWindow(nums: 'List[int]', k: int):
    if k==0 and len(nums) ==0: return []
    output = []
    i = 0
    for i in range(len(nums) - (k - 1)):
        output.append(max(nums[i:i + k]))
    return output


print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(maxSlidingWindow([], 0))

