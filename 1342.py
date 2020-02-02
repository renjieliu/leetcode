class Solution:
    def minSetSize(self, arr: 'List[int]') -> int:
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = 0
            hmp[a] +=1
        target = len(arr)//2  #(len(arr) +1)//2 # the length will be even per desc, for odd length, +1 //2 , for even length,+1//2 will not change the result
        s = 0
        cnt = 0
        lst = sorted(hmp.values(), reverse = True) # this value shows the occurrance of the number
        #print(lst)
        for v in lst:
            s+=v
            cnt+=1
            if s >=target:
                return cnt
