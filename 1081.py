class Solution:
    def smallestSubsequence(self, text: str) -> str:
        hmp = {}
        for c in text:
            if c not in hmp:
                hmp[c] = 0
            hmp[c] += 1
        output = []
        for c in text:
            hmp[c] -= 1
            if c not in output:
                while output and output[-1] > c and hmp[output[-1]] > 0:
                    output.pop()
                output.append(c)
            #print(hmp)
        return ''.join(output)