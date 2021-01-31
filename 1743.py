class Solution:
    def restoreArray(self, adjacentPairs: 'List[List[int]]') -> 'List[int]':
        hmp = defaultdict(list)
        for a, b in adjacentPairs:
            hmp[a].append(b)
            hmp[b].append(a)
        output = []
        added = set()
        for k, v in hmp.items():
            if len(v) == 1:
                output.append(k)  # get the first item
                added.add(output[-1])
                output.append(v[0])
                added.add(output[-1])
                del hmp[k]
                break
                # print(hmp)
        prev = output[-1]
        while len(hmp) > 0:
            for v in hmp[prev]:
                if v not in added:
                    output.append(v)
                    added.add(v)
            del hmp[prev]
            prev = output[-1]

        return output

