class Solution:
    def executeInstructions(self, n: int, startPos: 'List[int]', s: str) -> 'List[int]':
        hmp = {"R":[0,1], "L":[0,-1], "U": [-1,0], "D": [1,0]}
        output = []
        for i in range(len(s)):
            r = startPos[0]
            c = startPos[1]
            steps = 0 
            for j in range(i, len(s)):
                r += hmp[s[j]][0]
                c += hmp[s[j]][1]
                if -1 < r < n and -1 < c < n :
                    steps +=1
                else:
                    break
            output.append(steps)
        return output
    
