class Solution:
    def getDistances(self, arr: 'List[int]') -> 'List[int]':
        hmp = {}
        for i, c in enumerate(arr): # record the number location
            if c not in hmp:
                hmp[c] = []
            hmp[c].append(i)
                    
        output = []
        
        pre = {} #to record the prefix sum
        for k, v in hmp.items():
            pre[k] = [v[0]]
            curr = 0 
            for val in v[1:]:
                pre[k].append(pre[k][-1] + val)
                
        
        for loc, v in enumerate(arr):
            cnt_less = bisect.bisect_left(hmp[v], loc)
            # print(v, hmp[v], loc, cnt_less)
            if cnt_less == 0 or cnt_less == len(hmp[v]): #current is the smallest or largest
                output.append(abs(sum(hmp[v]) - loc*len(hmp[v])))
            else:
                A = loc*cnt_less - pre[v][cnt_less-1] # total before current loc
                B = pre[v][-1] - pre[v][cnt_less-1] - loc*(len(hmp[v]) - cnt_less) # total after current loc
                output.append(A+B)
        
        return output
        


