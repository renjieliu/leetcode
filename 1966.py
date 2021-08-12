class Solution:
    def binarySearchableNumbers(self, nums: 'List[int]') -> int:
        leftMax = [-float('inf')] #to find the Max on the left
        for i in range(1, len(nums)):
            leftMax.append(max(leftMax[-1], nums[i-1]))

        rightMin = [float('inf')] # to find the min on the right
        for i in range(len(nums)-2, -1, -1):
            rightMin.append(min(rightMin[-1], nums[i+1]))
        rightMin = rightMin[::-1]

        # print(leftMax, rightMin)
        cnt = 0
        for i in range(len(nums)):
            if leftMax[i] < nums[i] < rightMin[i]: #all n on the left is < curr and all n on the right is > curr
                cnt +=1
        return cnt



