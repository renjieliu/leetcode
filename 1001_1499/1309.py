class Solution:
    def freqAlphabets(self, s: str) -> str:
        hmp = {}
        for i in range(1, 10):
            hmp[str(i)] = chr(i + 96)
        for i in range(10, 27):
            hmp[str(i) + '#'] = chr(i + 96)

        output = ""
        while s:
            if len(s) >= 3 and s[2] == "#":
                output += hmp[s[:3]]
                s = s[3:]
            else:
                output += hmp[s[0]]
                s = s[1:]
        return output
