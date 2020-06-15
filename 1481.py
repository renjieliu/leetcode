class Solution:
    def findLeastNumOfUniqueInts(self, arr: 'List[int]', k: int) -> int:
        hmp = {}
        for a in arr:
            if a not in hmp:
                hmp[a] = 0
            hmp[a] += 1
        stk = sorted(hmp.values())
        cnt = 0
        while cnt < k:
            cnt += stk.pop(0)

        return len(stk) if cnt == k else len(stk) + 1  # +1 due to current number has some left
