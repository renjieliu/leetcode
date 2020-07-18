class Solution:
    def calculate(self, s: str) -> int:
        def calc(txt):
            a = txt.replace('--','+').replace('-','+-').split('+')
            return sum([int(x) for x in a if x != ""]) #for (-1), it will be split to ["", "-1"]
        s = s.replace(' ', '')
        cook = "" #the outer string
        stk = []
        for i,c in enumerate(s):
            if c == "(":
                stk.append("") #put following to a stk
            elif c== ")":
                localRes= str(calc(stk.pop())) #compute the current string
                if stk: #add current to the previous
                    stk[-1]+=localRes
                else:
                    cook+=localRes
            else:
                if stk == []:
                    cook += c
                else:
                    stk[-1] += c
        return calc(cook)