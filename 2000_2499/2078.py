class Solution:
    def maxDistance(self, colors: 'List[int]') -> int:
        output = -float('inf')
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    output=max(output, j-i)
        return output
            
