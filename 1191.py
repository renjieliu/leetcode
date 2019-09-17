def kConcatenationMaxSum(arr: 'List[int]', k: int):
    def kadane(arr):
        curr_max = 0
        curr = 0
        for i in range(len(arr)):
            curr = max(arr[i], curr+arr[i])
            curr_max = max(curr, curr_max)

        return 0 if curr_max<0 else curr_max

    if k ==1:
        return kadane(arr)
    else:
        mod = 10**9+7
        s = sum(arr)
        if s < 0:
            return kadane(arr*2) % mod
        else:
            return (s*(k-2) + kadane(arr*2) ) % mod



print(kConcatenationMaxSum(arr = [-1,-2], k = 1))
print(kConcatenationMaxSum(arr = [1,-2,1], k = 5))
print(kConcatenationMaxSum(arr = [1,2], k = 3))





