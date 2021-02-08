class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hmp = {}
        start_loc = 0
        output = 0
        for i, c in enumerate(s):  # eceba
            if c not in hmp:
                if len(hmp) == 2:
                    lst = list(hmp.keys())
                    if hmp[lst[0]][-1] < hmp[lst[1]][-1]:  # remove the one ends first, and get the new start_loc
                        t = hmp[lst[0]][-1]
                        del hmp[lst[0]]
                        while hmp[lst[1]][0] < t:
                            hmp[lst[1]].pop(0)
                        start_loc = hmp[lst[1]][0]
                    else:
                        t = hmp[lst[1]][-1]
                        del hmp[lst[1]]
                        while hmp[lst[0]][0] < t:
                            hmp[lst[0]].pop(0)
                        start_loc = hmp[lst[0]][0]

                    hmp[c] = [i]
                    output = max(output, (i - start_loc) + 1)
                else:
                    hmp[c] = [i]
                    output = max(output, (i - start_loc) + 1)
            else:
                hmp[c].append(i)
                output = max(output, (i - start_loc) + 1)

            # print(hmp, c, output)

        return output




