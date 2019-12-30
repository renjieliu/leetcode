class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hmp = {}
        for i in range(len(keyboard)):
            hmp[keyboard[i]] = i
        prev = 0
        output = 0
        for c in word:
            output += abs(hmp[c]-prev)
            prev = hmp[c]
        return output