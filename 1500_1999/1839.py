class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        output = 0
        l = r = 0
        stk = []
        while r < len(word):
            if word[r] == "a":
                if stk == []:#start of the string
                    l = r
                    stk.append(1)
                else:
                    if len(stk) == 1: # a is there in the stk
                        stk[-1] += 1
                    else: #not only a in the stk
                        stk = [1]
                        l = r
            elif word[r] == "e":
                if len(stk) == 1:
                    stk.append(1)
                else:
                    if len(stk) == 2: # a, e is there in the stk
                        stk[-1] += 1
                    else:
                        stk = []
            elif word[r] == "i":
                if len(stk) == 2:
                    stk.append(1)
                else:
                    if len(stk) == 3: # a, e, i is there in the stk
                        stk[-1] += 1
                    else:
                        stk = []
            elif word[r] == "o":
                if len(stk) == 3:
                    stk.append(1)
                else:
                    if len(stk) == 4: # a, e, i, o is there in the stk
                        stk[-1] += 1
                    else:
                        stk = []

            elif word[r] == "u":
                if len(stk) == 4:
                    stk.append(1)
                    output = max(output, r-l+1)
                else:
                    if len(stk) == 5: # a, e, i, o, u is there in the stk
                        stk[-1] += 1
                        output = max(output, r-l+1)
                    else:
                        stk = []
            # print(word[r], stk, output)
            r+=1
        return output