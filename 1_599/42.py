class Solution:
    def trap(self, height: 'List[int]') -> int:
        output = 0
        l = 0
        r = len(height) - 1
        leftMax = rightMax = 0
        while l <= r:
            if height[l] < height[r]:
                if height[l] > leftMax:
                    leftMax = height[l]
                else:
                    output += leftMax - height[l]  # water can be stored from leftMax to curr
                l += 1
            else:
                if height[r] > rightMax:
                    rightMax = height[r]
                else:
                    output += rightMax - height[r]  # water can be stored from rightMax to curr
                r -= 1
        return output

