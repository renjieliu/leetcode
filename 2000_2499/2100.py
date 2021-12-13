class Solution:
    def goodDaysToRobBank(self, security: 'List[int]', time: int) -> 'List[int]':
        if time == 0:
            return list(range(len(security)))
        slope_left = [0] #to record where does the left slope starts
        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                slope_left.append(slope_left[-1])
            else:
                slope_left.append(i)
        slope_right = [len(security)-1] #to record where the right slope ends
        output = []
        for i in range(len(security)-2, -1, -1):
            if security[i] <= security[i+1]:
                slope_right.append(slope_right[-1])
                if i-slope_left[i] >= time and slope_right[-2]-i >= time: #the left slope start <= i-time and the right slope ends >= i+time
                    output.append(i)
            else:
                slope_right.append(i)
        # print(slope_left, slope_right)
        return output
    
