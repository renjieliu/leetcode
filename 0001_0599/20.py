class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        left = ['(', '[', '{']
        for c in s:
            if c in left:
                stk.append(c)
            else:
                if stk:
                    if  stk.pop() + c not in ['()', '[]', '{}']:
                        return False
                else:
                    return False
            #print(c, 'stk' ,stk)
        return stk == []

