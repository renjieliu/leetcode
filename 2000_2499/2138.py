class Solution:
    def divideString(self, s: str, k: int, fill: str) -> 'List[str]':
        output = []
        curr = "" 
        for i in range(len(s)):
            curr += s[i] 
            if (i+1) % k == 0:
                output.append(curr)
                curr = ""
        if curr: 
            output.append(curr)
        output[-1] = output[-1] + fill * (k-len(output[-1]))
        return output
    
    
    