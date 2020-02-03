class Solution:
    def boldWords(self, words: 'List[str]', S: str) -> str:
        def findAll(SS, ss):  # find all the ss in the SS
            output = []
            i = 0
            while i < len(SS) + 1 - len(ss):
                if SS[i:i + len(ss)] == ss:
                    output.append([i, i + len(ss) - 1])
                i += 1
            return output

        if S == "":
            return ""
        elif words == []:
            return S
        else:
            arr = []
            for w in words:
                pos = findAll(S, w)  # find all the position of w in S
                if findAll(S, w) != []:
                    arr += pos
            if len(arr) == 0: return S
            merged = []
            arr.sort()
            while arr:  # to merge the positions need to be bolded
                merged.append(arr.pop(0))
                i = 0
                while arr:
                    if merged[-1][0] <= arr[0][0] <= merged[-1][1] or merged[-1][0] <= arr[0][0] <= merged[-1][
                        1] + 1:  # if itself is within the range, or it can ba made continuous
                        merged[-1] = [min(arr[0][0], merged[-1][0]), max(arr[0][1], merged[-1][1])]
                        arr.pop(0)
                    else:
                        break
            output = ""
            i = 0
            currCheck = merged.pop(0)
            while i < len(S):  # if the position is in the merged, then append bold mark
                if i == currCheck[0] == currCheck[1]:
                    output += '<b>' + S[i] + '</b>'
                    if len(merged) > 0:
                        currCheck = merged.pop(0)
                elif i == currCheck[0]:  # start pos
                    output += '<b>' + S[i]
                elif i == currCheck[1]:  # end pos
                    output += S[i] + '</b>'
                    if len(merged) > 0:
                        currCheck = merged.pop(0)
                else:
                    output += S[i]
                i += 1
            return output























