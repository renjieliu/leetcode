class Solution:
    def maxRepOpt1(self, text: str) -> int:
        hmp = {text[0]: [[0]]}
        for i in range(1, len(text)): # if continuous, they put them in the same array
            if text[i] == text[i-1]:
                hmp[text[i]][-1].append(i)
            else:
                if text[i] not in hmp:
                    hmp[text[i]] = []
                hmp[text[i]].append([i])
        #print(hmp)
        output = 0
        for k, v in hmp.items(): #for each value array, check if the gap is 2, if it is, it can be filled. if not, it can only be increased by 1.
            if len(v) ==1:
                output = max(output, len(v[0]))
            else:
                for i in range(1, len(v)):
                    if v[i][0] - v[i-1][-1] == 2: #only 1 gap
                        output = max(output, len(v[i-1]) + len(v[i]) + (1 if len(v) >2 else 0) ) # the gap can be moved to
                    else: #the gap is more than 2, only one can be extended.
                        output = max(output, 1+ max(len(v[i-1]),len(v[i])))
        return output
