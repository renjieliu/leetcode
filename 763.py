class Solution:
    def partitionLabels(self, S: str) -> 'List[int]':
        hmp = {}
        for i, c in enumerate(S):
            if c not in hmp:
                hmp[c] = []

            if len(hmp[c]) == 2:
                hmp[c][-1] = i
            else:
                hmp[c].append(i)
        output = []
        ranges = sorted(hmp.values())
        prev = ranges[0]
        for curr in ranges[1:]:
            if curr[0] > prev[-1]:  # r > prevend, then it can be cut here.
                output.append(prev[-1] - prev[0] + 1)
                prev = curr
            else:
                if curr[0] < prev[-1] and curr[-1] > prev[-1]:  # curr range is extending th prevend
                    prev[-1] = curr[1]

        output.append(prev[-1] - prev[0] + 1)  # add the last section
        return output

