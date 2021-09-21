class Solution:
    def findOriginalArray(self, changed: 'List[int]') -> 'List[int]':
        if len(changed) % 2 == 1 :
            return []
        else:
            changed.sort()
            hmp = {} #counter for the original arr
            double = {} #record the doubled number of curr
            for c in changed:
                if c not in hmp:
                    hmp[c] = 0
                hmp[c] += 1

            output = []
            for c in changed:
                if c in double: #itself if a double of some prev number
                    double[c] -= 1
                    if double[c] == 0:
                        del double[c]
                elif c*2 in hmp: #check if doubled is in the hmp
                    if c*2 not in double:
                        double[c*2] = 0
                    double[c*2] += 1
                    output.append(c)
                else: #not as doubled of some number, and doubled self not in arr
                    return []
            return output if double == {} else [] # double need to be cleared.



