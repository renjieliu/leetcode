def maxArea(height: 'List[int]') -> int:
    left, right = 0, len(height) - 1
    maxSize = 0
    while left < right:
        if height[left] < height[right]:
            maxSize = max((right - left) * height[left], maxSize)
            left += 1
        else:
            maxSize = max((right - left) * height[right], maxSize)
            right -= 1

    return maxSize

# Below is the O(n2)approach, time limited exceeded.

#  def maxArea(self, height: List[int]) -> int:
#      maxsize  = 0
#      for i in range(len(height)):
#          if height[i] != 0:
#              for j in range(maxsize//height[i]+1, len(height)):  #only the one after max//height[i] has a chance to beat the current max
#                  maxsize = max(min(height[i],height[j] )*(j-i), maxsize)
#      return max

print(maxArea([1,8,6,2,5,4,8,3,7]))