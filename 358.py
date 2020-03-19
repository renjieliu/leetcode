class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if len(s) <= 1 or k <= 1: return s
        hmp = {}
        for c in s:
            if c not in hmp:
                hmp[c] = []
            hmp[c].append(c)
        keylist = sorted(hmp.keys(), key=lambda x: len(hmp[x]), reverse=True)
        if len(hmp) < k: return ""  # meaning the character will spill over to the next group
        output = ""
        curr = ""
        while keylist:
            cnt = 0
            curr = ""
            i = 0
            while i < len(keylist):
                t = keylist[i]
                curr += hmp[t].pop()
                if hmp[t] == []:
                    keylist.remove(t)
                    del hmp[t]
                else:
                    i += 1
                if len(curr) == k:
                    output += curr
                    curr = ""
                    keylist = sorted(hmp.keys(), key=lambda x: len(hmp[x]), reverse=True)
                    if keylist and len(keylist) < k and len(hmp[keylist[0]]) > 1: return ""
                    # print(keylist)
                    break
        output += curr
        return output

# split into groups approach does not work.
#         if len((hmp[keylst[0]])) > len(s)//k + (1 if len(s)%k != 0 else 0): return "" #meaning the character will spill over to the next group
#         group = [len(s)//k + 1 ] *  (len(s) % k)  #for the first rem group, each one has 1 more
#         group += [len(s)//k] * (k-len(s)%k) #the remaining of the group
#         flat = []
#         for i in keylst:
#             flat+=hmp[i]
#         s = 0
#         pool = []
#         for g in group:
#             pool.append(flat[s:s+g])
#             s += g
#             if len(pool) > 1 and pool[-1][0] == pool[-2][0]: return ""  #for ones like [['c'], ['c']]
#         #print(pool)
#         output = ""
#         while pool:
#             i = 0
#             while i < len(pool):
#                 output+=pool[i].pop(0)
#                 if pool[i] == []:
#                     pool = pool[:i] + pool[i+1:]
#                 else:
#                     i+=1
#         return output