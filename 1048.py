class Solution:
    def longestStrChain(words: 'List[str]') -> int:
        def onediff(s1, s2):  # using s1 is the short and s2 as the long
            p1 = p2 = err = 0
            while p1 < len(s1):
                if s1[p1] != s2[p2]:
                    p1 -= 1  # p1 stay at the same place after the iteration
                    err += 1
                    if err > 1:
                        return 0
                p1 += 1
                p2 += 1

            return 1

        dp = []
        len_dict = {}
        ref = sorted(words, key=lambda x: len(x))  # sort by the length of the words
        output = 1
        for i in range(len(ref)):
            if output == 16: print(len_dict, dp)
            w = ref[i]
            l = len(w)
            if l not in len_dict:
                len_dict[l] = []
            len_dict[l].append(i)  # add the word index to the length hash

            if l == 1:
                dp.append(1)
                output = max(output, 1)
            else:  # to check if the len()-1 exist in the hash table , if not dp append curr = 1. If it does, find if it can find a word with diff = 1
                if l - 1 not in len_dict:
                    dp.append(1)
                    output = max(output, 1)
                else:
                    m = 1
                    for j in len_dict[l - 1]:
                        if onediff(ref[j], w) == 1:  # only one position different
                            m = max(m, dp[j] + 1)
                    dp.append(m)
                    output = max(m, output)

        return output


