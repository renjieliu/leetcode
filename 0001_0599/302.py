class Solution:
    def minArea(self, image: 'List[List[str]]', x: int, y: int) -> int: #O(MN), not the best solution. 
        arr = [float('inf'), float('inf'), -float('inf'), -float('inf')] # find the upper, left, bottom, and right corner
        for r in range(len(image)):
            for c in range(len(image[0])):
                if image[r][c]  == "1":
                    arr[0] = min(r, arr[0])
                    arr[1] = min(c, arr[1])
                    arr[2] = max(r, arr[2])
                    arr[3] = max(c, arr[3])
        return (arr[2]-arr[0] + 1) * (arr[3]-arr[1]+1)



                
    
