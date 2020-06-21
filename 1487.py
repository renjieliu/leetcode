class Solution:
    def getFolderNames(self, names: 'List[str]') -> 'List[str]':
        hmp = {}
        output = []
        for n in names:
            if n not in hmp:
                output.append(n)
                hmp[n] = 1
            else:
                i = hmp[n]
                while n + "(" + str(i) + ")" in hmp:
                    i += 1
                output.append(n + "(" + str(i) + ")")
                hmp[n + "(" + str(i) + ")"] = 1
                hmp[n] = i

        return output