class Solution:
    def trap(self, height: 'List[int]') -> int: # O( N | N )
        dp_left = [height[0]]  # max height on the left 
        
        for i in range(1, len(height)): 
            dp_left.append(max(height[i], dp_left[-1]))
        
        dp_right = [height[-1]] # max height on the right 
        for i in range(len(height)-2, -1, -1):
            dp_right.append(max(height[i], dp_right[-1])) 
        
        dp_right = dp_right[::-1] #reverse the dp, to make it same order as original array
        
        output = 0
        
        for i in range(1, len(height)):
            output += min(dp_left[i], dp_right[i]) - height[i]
        
        return output
    


# previous solution

# class Solution:
#     def trap(self, height: 'List[int]') -> int:
#         output = 0
#         l = 0
#         r = len(height) - 1
#         leftMax = rightMax = 0
#         while l <= r:
#             if height[l] < height[r]:
#                 if height[l] > leftMax:
#                     leftMax = height[l]
#                 else:
#                     output += leftMax - height[l]  # water can be stored from leftMax to curr
#                 l += 1
#             else:
#                 if height[r] > rightMax:
#                     rightMax = height[r]
#                 else:
#                     output += rightMax - height[r]  # water can be stored from rightMax to curr
#                 r -= 1
#         return output

