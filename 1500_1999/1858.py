class Solution:
    def longestWord(self, words: 'List[str]') -> str:
        words = set(words)
        output = ""
        for w in words:
            valid = 1
            for i in range(1, len(w)): #check all the possible prefix
                if w[:i] not in words:
                    valid = 0
                    break
            if valid:
                if len(w) > len(output):
                    output = w
                elif len(w) == len(output):
                    output = min(w, output)
        return output
