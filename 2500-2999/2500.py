class Solution:
    def deleteGreatestValue(self, grid: 'List[List[int]]') -> int: # O( N**2logN | MN )
        arr = []
        for r in grid: #sorted each row, and add to the arr
            arr.append(sorted(r, reverse = True))
        
        output = 0 
        for c in range(len(arr[0])): # find max of each col
            curr = -float('inf')
            for r in range(len(arr)):
                curr = max(arr[r][c], curr)
            output += curr
        
        return output


    
