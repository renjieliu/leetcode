class Solution:
    def anagramMappings(self, A: 'List[int]', B: 'List[int]'):
        hmp = {}
        for i in range(len(B)):
            if B[i] not in hmp:
                hmp[B[i]] = []
            hmp[B[i]].append(i)
        output = []
        for a in A:
            output.append(hmp[a].pop())
        return output
