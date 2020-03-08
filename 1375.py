class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        left = 0 # meaning how many left number should be there
        output = 0
        currMax = 0
        for n in light:
            if n < currMax:
                left -=1 # put to the left
                if left == 0:
                    output+=1
            else:
                left = left + n - currMax - 1 # to be filled
                if left == 0:
                    output +=1 
                currMax = n 
            #print(n, currMax, left)
        return output

            