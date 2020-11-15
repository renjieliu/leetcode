class Solution:
    def minOperations(self, nums: 'List[int]', x: int) -> int:
        if sum(nums) < x:
            return -1
        A = float('inf')
        t = x
        for i, c in enumerate(nums):  # sliding from the left
            t -= c
            if t == 0:
                A = i + 1
        B = float('inf')
        t = x
        for i, c in enumerate(nums[::-1]):  # sliding from the right
            t -= c
            if t == 0:
                B = i + 1
                # sliding from both side
        sum_left = [nums[0]]
        for n in nums[1:]:
            sum_left.append(sum_left[-1] + n)
        right = {}
        curr = 0
        find = [float('inf')]
        for i, c in enumerate(nums[::-1]):
            curr += c
            right[curr] = i

        for i, c in enumerate(sum_left):
            if x - c in right:  # the combination exists
                action = i + 1 + right[x - c] + 1
                if action <= len(nums):
                    find.append(action)

        C = min(find)

        output = min(A, B, C)

        return -1 if output == float('inf') else output













