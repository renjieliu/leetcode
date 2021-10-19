class Solution:
    def sumOfBeauties(self, nums: 'List[int]') -> int:
        left = [-float('inf')]
        for n in nums[:-1]: #max on the left
            left.append(max(left[-1], n))
        right = [nums[-1]]
        for n in nums[::-1][:-1]: #min on the right
            right.append(min(n, right[-1]))
        right = right[::-1]
        output = 0
        for i in range(1, len(nums)-1): # to check if curr satisfy condition 1 or condition 2
            curr = nums[i]
            if left[i] < curr < right[i]:
                output += 2
            elif nums[i-1] < curr < nums[i+1]:
                output += 1
            else:
                output += 0

        return output

