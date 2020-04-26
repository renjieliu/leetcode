class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if len(croakOfFrogs) < 5: return -1 #cannot finish
        c = r = o = a = 0
        frogsInAction = 0
        frogsInRest = 0
        for n in croakOfFrogs:
            if n == 'c': #need a new frog , either from the resting frog, or add a new one
                if frogsInRest != 0:
                    frogsInRest-=1
                frogsInAction+=1
                c+=1
            elif n=='r':
                if c > 0:
                    r+=1
                else:
                    return-1
            elif n=="o":
                if c > 0 and r > 0:
                    o+=1
                else:
                    return -1
            elif n =="a":
                if c > 0 and r > 0 and o > 0:
                    a+=1
                else:
                    return -1
            elif n =="k":
                if c > 0 and r > 0 and o > 0 and a> 0:
                    c-=1
                    r-=1
                    o-=1
                    a-=1
                    frogsInAction-=1
                    frogsInRest+=1
                else:
                    return -1
        return frogsInRest if c==r==o==a==frogsInAction==0 else -1