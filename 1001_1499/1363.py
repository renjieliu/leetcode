class Solution:
    def largestMultipleOfThree(self, digits: 'List[int]') -> str:
        digits.sort(reverse = True)
        s = sum(digits)
        more = s%3 
        if more == 0:
            output = ""
            for d in digits:
                output+=str(d)
            return '0' if output.count('0') == len(output) and len(output)>0 else output 
        for i in range(len(digits)-1, -1, -1): 
            if digits[i]%3==more: #if can find a number%3 == more, take it out.
                output = ""
                j = 0
                while j < len(digits):
                    if j!= i:
                        output+=str(digits[j])
                    j+=1
                return '0' if output.count('0') == len(output) and len(output)>0 else output 
        if more == 1:  #more is 1 or 2 
            t = []
            for i in range(len(digits)-1, -1, -1): # to find 2 number added to the more
                if digits[i]%3 ==2:
                    t.append(i)
                    if len(t) == 2: 
                        output = ""
                        j = 0
                        while j < len(digits):
                            if j not in t:
                                output+=str(digits[j])
                            j+=1
                        return '0' if output.count('0') == len(output) and len(output)>0 else output 
            return ""
        elif more == 2:
            t = []
            for i in range(len(digits)-1, -1, -1): # to find 2 number added to the more
                if digits[i]%3 == 1:
                    t.append(i)
                    if len(t) == 2: 
                        output = ""
                        j = 0
                        while j < len(digits):
                            if j not in t:
                                output+=str(digits[j])
                            j+=1
                        return '0' if output.count('0') == len(output) and len(output)>0 else output 
            return ""
            
            
            
            
       