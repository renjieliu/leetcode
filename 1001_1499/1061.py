class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        hmp = {}
        for i in range(len(A)):
            a = A[i]
            b = B[i]
            if a not in hmp:
                hmp[a] = []
            hmp[a].append(b)
            hmp[a].append(a)
            if b not in hmp:
                hmp[b] = []
            hmp[b].append(a)
            hmp[b].append(b)
        output = ""
        for k, v in hmp.items():
            path = ""
            curr = list(set(v)).copy()
            i = 0
            while i < len(curr):
                c = curr[i]
                if c not in path and c in hmp:
                    path += c
                    curr += hmp[c]
                i += 1
            hmp[k] = sorted(list(set(curr)))
        # print(hmp)
        for c in S:
            if c not in hmp:
                output += c
            else:
                output += hmp[c][0]
        return output
