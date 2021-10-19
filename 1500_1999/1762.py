class Solution:
    def findBuildings(self, heights: 'List[int]') -> 'List[int]':
        output = [len(heights)-1]
        currMax = heights[-1]
        for i in range(len(heights)-2,-1,-1): #if curr element is > currMax, then it has an ocean view
            if heights[i] > currMax:
                output.append(i)
                currMax = heights[i]
        return output[::-1] #the result should be 0 based, sorted ascendingly.
