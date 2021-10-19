class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: 'List[str]') -> 'List[List[str]]':
        wordSet = set(wordList)  # to check if a word is existed in O(1)

        def neighbors(word):
            for i in range(len(word)):  # change every possible single letters and check if it's in wordSet
                for c in ascii_lowercase:
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordSet:
                        yield newWord

        layer = {}
        layer[beginWord] = [[beginWord]]  # layer[word] is all possible sequence paths which start from beginWord and end at `word`.
        while layer.keys():
            nextLayer = defaultdict(list)
            for word in layer.keys():
                if word == endWord:
                    return layer[word]  # return all shortest sequence paths
                for nei in neighbors(word):
                    for path in layer[word]:
                        nextLayer[nei].append(path + [nei])  # add new word to all sequences and form new layer element
            wordSet -= set(nextLayer.keys())  # remove visited words to prevent loops
            layer = nextLayer  # move to new layer

        return []

