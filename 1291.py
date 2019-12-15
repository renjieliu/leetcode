class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def construct(digit):
            output = []
            for i in range(1, 10-digit+1): #add first digits
                temp = str(i)
                for j in range(1, digit): #add remaining digits
                    temp+= str(int(temp[-1])+1)
                output.append(int(temp))
            return output
                
        start = len(str(low))
        end = len(str(high))
        pool = []
        for i in range(start, end+1):
            pool += construct(i)
        output =[] 
        for i in pool:
            if low<=i <=high:
                output.append(i)
        return output