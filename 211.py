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
        for i in range(1, len(word)):
            if word[i] not in curr:
                curr[word[i]] = {}
            curr = curr[word[i]]
        curr[0] = None  # end of a path

    def helper(self, curr, trie):
        if trie == None:
            return False
        elif curr == "":
            return 0 in trie
        local_trie = trie
        for i in range(len(curr)):
            c = curr[i]
            if c != ".":
                if c not in local_trie:
                    return False
                else:
                    local_trie = local_trie[c]
            elif c == ".":  # to test each key
                if local_trie == None: return False
                for k in local_trie.keys():
                    if self.helper(curr[i + 1:], local_trie[k]) == True:
                        return True
                return False
        return 0 in local_trie

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.helper(word, self.trie)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)