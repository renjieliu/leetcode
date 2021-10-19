class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        output = 0 
        maxTimes = len(sequence) // len(word)
        for i in range(1, maxTimes+1):
            if word*i in sequence:
                output = i
        return output