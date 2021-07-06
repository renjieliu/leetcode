class Solution:
    def minSetSize(self, arr: 'List[int]') -> int:
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = 0
            hmp[a]+=1
        curr = 0
        cnt = 0
        stk = sorted(hmp.values())
        while curr < len(arr)//2:
            curr += stk.pop() # pop from right to left, meaning popping from largest to smallest
            cnt += 1
        return cnt
