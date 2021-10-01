class Solution:
    def brightestPosition(self, lights: 'List[List[int]]') -> int:
        hmp = defaultdict(int) # same approach as range sum, but only check the start and end point for each range
        for a, b in lights:
            hmp[a-b] += 1
            hmp[a+b+1] -= 1 #the light cannot reach a+b+1 point
        output = lights[0][0]
        globalMax = -float('inf')
        curr = 0
        for k in sorted(hmp.keys()):
            curr += hmp[k]
            if curr > globalMax:
                globalMax = curr
                output = k
        return output


