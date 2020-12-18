class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> bool:
        minStk = [nums[0]]
        for n in nums[1:]:  # find the minStk up to curr
            minStk.append(min(minStk[-1], n))
        maxStk = [nums[-1]]
        for n in nums[:-1][::-1]:  # find the max on the right
            maxStk.append(max(maxStk[-1], n))
        maxStk = maxStk[::-1]

        for i in range(len(nums)):  # check if there's smaller on the left, and larger on the right
            if minStk[i] < nums[i] < maxStk[i]:
                return True
        return False

