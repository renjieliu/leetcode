class Solution:
    def countPairs(self, deliciousness: 'List[int]') -> int:
        mod = 10**9+7
        power = [2**_ for _ in range(22)]
        deliciousness.sort()
        hmp = {}
        for i, d in enumerate(deliciousness):
            if d not in hmp:
                hmp[d] = []
            hmp[d].append(i)

        cnt = 0
        for i, d in enumerate(deliciousness):
            for p in power:
                rem = p-d
                if rem in hmp:
                    while hmp[rem] and hmp[rem][0] <= i: #check how many is after the current number
                        hmp[rem].pop(0)
                    if hmp[rem] == []:
                        del hmp[rem]
                    else:
                        cnt += len(hmp[rem])

        return cnt%mod