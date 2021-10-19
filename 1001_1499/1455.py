class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for i, c in enumerate(sentence.split(' ')):
            if searchWord == c[:len(searchWord)]:
                return i + 1
        return -1
