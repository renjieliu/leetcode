class Solution:
    def countLargestGroup(self, n: int) -> int:
        hmp = {}
        output = {}
        maxx = -float('inf')
        for i in range(1, n + 1):
            t = sum(map(lambda x: int(x), list(str(i))))
            if t not in hmp:
                hmp[t] = []
            hmp[t].append(i)

            maxx = max(len(hmp[t]), maxx)

            if len(hmp[t]) not in output:
                output[len(hmp[t])] = 0
            output[len(hmp[t])] += 1

        return output[maxx]