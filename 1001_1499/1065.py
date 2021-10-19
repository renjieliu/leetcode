class Solution:
    def indexPairs(self, text: str, words: 'List[str]') -> 'List[List[int]]':
        output = []
        for w in words:
            i = 0
            while i < len(text) - len(w) + 1:
                if text[i:i + len(w)] == w:
                    output.append([i, i + len(w) - 1])
                i += 1
        return sorted(output)
