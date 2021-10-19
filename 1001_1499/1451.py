class Solution:
    def arrangeWords(self, text: str) -> str:
        return (' '.join(sorted(text.split(' '), key = lambda x: len(x)))).capitalize()