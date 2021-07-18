class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(0 if set(w) & set(brokenLetters) else 1 for w in text.split(' '))
