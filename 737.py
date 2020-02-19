class Solution:
    def areSentencesSimilarTwo(self, words1: 'List[str]', words2: 'List[str]', pairs: 'List[List[str]]') -> bool:
        def find(a, tree):  # find the root of a in t
            if a not in tree:
                tree[a] = a
                return a
            while a in tree and tree[a] != a:
                a = tree[a]
            return a

        tree = {}
        for a, b in pairs:  # try to link a tree to b tree
            a1 = find(a, tree)
            b1 = find(b, tree)
            tree[a1] = b1
        if len(words1) != len(words2):
            return False
        i = 0
        while i < len(words1):
            if find(words1[i], tree) != find(words2[i], tree):
                return False
            i += 1
        return True


