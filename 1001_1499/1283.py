class Solution:
    def smallestDivisor(self, nums: 'List[int]', threshold: int) -> int:
        def calc(arr, n):
            output = 0
            for a in arr:
                A = a / n
                B = a // n
                output += B + (1 if A > B else 0)
            return output

        output = float('inf')
        s = 1
        e = max(nums)
        while s <= e:
            mid = s - (s - e) // 2

            if calc(nums, mid) > threshold:
                s = mid + 1
            else:
                output = min(mid, output)
                e = mid - 1
                # print(mid, calc(nums, mid))
        return output
