class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: 'List[List[int]]') -> str:
        if len(pairs) == 0: return s
        hmp = {}
        for p in pairs:  # O(n)
            if p[0] not in hmp:
                hmp[p[0]] = []
            hmp[p[0]].append(p[0])
            hmp[p[0]].append(p[1])
            if p[1] not in hmp:
                hmp[p[1]] = []
            hmp[p[1]].append(p[0])
            hmp[p[1]].append(p[1])
        group = []
        taken = {}
        for k in hmp.keys():  # using hmp to find the group, within the same group, all the character can swap anytime, find smallest of each group and merge
            if k not in taken:
                group.append(hmp[k])
                taken[k] = 1  # current key has been grouped
                i = 0
                while i < len(group[-1]):
                    c = group[-1][i]
                    if c in hmp and c not in taken:
                        group[-1] += hmp[c]  # all the related index to the current group
                        taken[c] = 1
                    i += 1
                group[-1] = sorted(list(set(group[-1])))  # remove duplicates

        words = []
        for p in group:  # for each p, find the corresponding character, concatenate and find the smallest it can turn to
            curr = []
            for c in p:
                curr.append(s[c])
            curr.sort()
            words.append(curr)
        output = [''] * len(s)
        for i in range(len(group)):  # index group
            for j in range(len(group[i])):  # find each index
                loc = group[i][j]
                output[loc] = words[i][j]  # find the smallest char for each index

        for i in range(len(output)):  # for the ones not in swap, use the one from s
            if output[i] == "":
                output[i] = s[i]

        return ''.join(output)























