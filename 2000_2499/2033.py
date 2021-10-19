class Solution:
    def minOperations(self, grid: 'List[List[int]]', x: int) -> int:
        arr = []
        for r in grid:
            for c in r:
                arr.append(c)
        arr.sort()
        n = arr[(len(arr)-1)//2] #pick the smaller middle number 
        output = 0
        for a in arr:
            if (n-a)%x:
                return -1
            output += abs(n-a)//x 
        return output


