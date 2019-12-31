class Solution:
    def countSteppingNumbers(self, low: int, high: int):
        start=len(str(low))
        end=len(str(high))
        pool = temp = prev = [str(_) for _ in range(10)]
        width = 1
        while width < end:
            temp = [] #current new array
            for p in prev: #array for the numbers with previous length
                if int(p[-1]) == 9:
                    temp.append(p+"8")
                elif int(p[-1]) == 0:
                    if len(p) > 1:
                        temp.append(p+"1")
                else:
                    temp.append(p+ str(int(p[-1]) + 1) )
                    temp.append(p+ str(int(p[-1]) - 1) )
            prev = temp
            pool+=temp
            width +=1
        output = []
        for i in pool:
            if low<=int(i) <=high:
                output.append(int(i))
        return sorted(output)