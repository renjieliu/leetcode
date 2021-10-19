class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        if word[0] not in self.trie:
            self.trie[word[0]] = {}
        curr = self.trie[word[0]]
        for c in word[1:]:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['$'] = None

    def helper(self, word, hmp):
        if len(word) == 0:
            return True if '$' in hmp else False

        i = 0
        while i < len(word):
            if word[i] in hmp:
                hmp = hmp[word[i]]
                i += 1
                if i == len(word):
                    return True if '$' in hmp else False

            else:
                if word[i] == ".":
                    for h in hmp.values():
                        if h != None and self.helper(word[i + 1:], h) == True:
                            return True
                    return False
                else:
                    return False

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.helper(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)