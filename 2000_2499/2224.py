class Solution:
    def convertTime(self, current: str, correct: str) -> int: #O(N | 1)
        curr = int(current[:2]) * 60 + int(current[-2:]) # convert to minute
        corr = int(correct[:2]) * 60 + int(correct[-2:]) # convert to minute
        
        def calc(a, b): # per description, curr <= correct, and it can only increase. No need to check reduce the scenario of reducing curr
            diff = b-a
            output = 0
            if diff>=60:
                oper = diff//60
                output += oper
                diff-=oper*60
            if diff >=15:
                oper = diff//15
                output += oper
                diff -= oper*15
            if diff >=5:
                oper = diff//5
                diff -= oper*5 
                output += oper
            return output + diff 
    
        return calc(curr, corr) 
                
