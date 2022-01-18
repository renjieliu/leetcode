class Solution:
    def divideString(self, s: str, k: int, fill: str) -> 'List[str]':
        output = []
        curr = "" 
        for i in range(len(s)): #read one by one and append. 
            curr += s[i] 
            if (i+1) % k == 0:
                output.append(curr)
                curr = ""
        if curr: 
            output.append(curr)
        output[-1] = output[-1] + fill * (k-len(output[-1])) #pad the last string if the length is less than the size k
        return output
    
    
    
    